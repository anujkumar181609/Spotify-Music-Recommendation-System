#import libraries
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime


#Page config
st.set_page_config(
    page_title="Spotify Music Recommender",
    page_icon="🎵",
    layout="wide"
)

#load data
@st.cache_data
def load_data():
    return pd.read_csv("spotify_tracks_with_clusters.csv")

df = load_data()

audio_features = [
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo'
]

#cluster names
cluster_names = {
    0: "🔥 High Energy Dance",
    1: "🎸 Acoustic & Emotional",
    2: "🎹 Instrumental & Ambient",
    3: "⚡ Workout & Party",
    4: "🎤 Live Performance",
    5: "🎙 Rap & Spoken",
    6: "🌙 Chill & Relaxing"
}

#greetings
hour = datetime.now().hour

if hour < 12:
    greeting = "🌅 Good Morning"
elif hour < 17:
    greeting = "☀️ Good Afternoon"
elif hour < 21:
    greeting = "🌇 Good Evening"
else:
    greeting = "🌙 Good Night"


#sidebar
with st.sidebar:

    st.title("🎵 Spotify Hybrid Music Recommender")

    st.markdown("---")

    st.subheader("📌 About Project")

    st.write("""
Spotify Hybrid Music Recommendation System using:

• K-Means Clustering

• Content-Based Filtering

• Cosine Similarity

Built on Spotify audio features such as:
danceability, energy, loudness,
valence and acousticness.
""")

    st.markdown("---")

    st.subheader("📊 Dataset")

    st.write(f"Songs: {len(df):,}")
    st.write(f"Clusters: {df['cluster'].nunique()}")

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.write("""
Python

Pandas

Scikit-Learn

Plotly

Streamlit
""")

    st.markdown("---")

    st.caption("Developed by Anuj Kumar")


#header
st.title(greeting)

st.markdown("""
# 🎧 Spotify Hybrid Music Recommendation System

Discover songs with similar audio characteristics using
K-Means clustering and cosine similarity.
""")

st.markdown("---")


#search box
df["display_name"] = (
    df["track_name"].astype(str)
    + " — "
    + df["artists"].astype(str)
)

song_options = sorted(df["display_name"].unique())

selected_display = st.selectbox(
    "🔍 Search Song",
    options=song_options,
    index=None,
    placeholder="Start typing a song name..."
)


#if song selected
if selected_display is not None:

    selected_row = df[
        df["display_name"] == selected_display
    ].iloc[0]

    #song info
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🎤 Artist",
            selected_row["artists"]
        )

    with col2:
        st.metric(
            "🎵 Cluster Type",
            cluster_names.get(
                selected_row["cluster"],
                f"Cluster {selected_row['cluster']}"
            )
        )

    st.markdown("---")

    #audio profile chart
    st.subheader("🎼 Audio Profile")

    chart_features = [
        "danceability",
        "energy",
        "speechiness",
        "acousticness",
        "liveness",
        "valence"
    ]

    values = selected_row[
        chart_features
    ].tolist()

    values += values[:1]

    labels = chart_features + [chart_features[0]]

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=labels,
            fill='toself',
            name='Audio Profile'
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,1]
            )
        ),
        showlegend=False,
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown("---")

    #recommendation function
    def recommend(song_index, top_n=5):

        selected_song = df.loc[song_index]

        cluster_id = selected_song["cluster"]

        cluster_songs = df[
            df["cluster"] == cluster_id
        ].copy()

        song_vector = selected_song[
            audio_features
        ].values.reshape(1, -1)

        similarities = cosine_similarity(
            song_vector,
            cluster_songs[audio_features]
        )[0]

        cluster_songs["similarity"] = similarities

        cluster_songs = cluster_songs[
            cluster_songs.index != song_index
        ]

        recommendations = cluster_songs.sort_values(
            by="similarity",
            ascending=False
        )

        return recommendations[
            [
                "track_name",
                "artists",
                "similarity"
            ]
        ].head(top_n)

    
    #button
    if st.button("🎶 Generate Recommendations"):

        recommendations = recommend(
            selected_row.name
        )

        recommendations = (
            recommendations
            .reset_index(drop=True)
        )

        recommendations["similarity"] = (
            recommendations["similarity"] * 100
        ).round(2)

        st.success(
            f"Recommendations for: {selected_row['track_name']}"
        )

        st.dataframe(
            recommendations.rename(
                columns={
                    "track_name": "Song",
                    "artists": "Artist",
                    "similarity": "Similarity (%)"
                }
            ),
            use_container_width=True
        )

#dataset insights
st.markdown("---")

st.subheader("📈 Dataset Insights")

c1, c2 = st.columns(2)

with c1:
    st.metric(
        "Total Songs",
        f"{len(df):,}"
    )

with c2:
    st.metric(
        "Total Clusters",
        df["cluster"].nunique()
    )


#cluster distribution
st.subheader("📊 Cluster Distribution")

cluster_counts = (
    df["cluster"]
    .value_counts()
    .sort_index()
)

st.bar_chart(cluster_counts)


#footer
st.markdown("---")

st.caption("""
Spotify Hybrid Music Recommendation System

K-Means Clustering + Content-Based Filtering + Cosine Similarity

Developed by Anuj Kumar
""")
