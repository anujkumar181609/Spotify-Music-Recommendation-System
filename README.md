# 🎵 Spotify Music Recommendation System

A Machine Learning-powered music recommendation system that suggests songs with similar audio characteristics using **K-Means Clustering** and **Cosine Similarity**.

The system analyzes Spotify audio features such as danceability, energy, loudness, valence, acousticness, tempo, and more to group songs into meaningful clusters and generate personalized recommendations.

### 🚀 Live Demo

[Spotify Music Recommendation System (Live App)](https://spotify-hybrid-music-recommendation-system-9aondm5hxu7cszo6mfc.streamlit.app/?utm_source=chatgpt.com)

---

# 📌 Project Overview

Traditional recommendation systems often require user history and ratings.

This project uses **content-based filtering** combined with **unsupervised learning** to recommend songs based solely on their musical characteristics.

### Recommendation Pipeline

```text
User Selects Song
        ↓
Find Song Cluster
        ↓
Fetch Songs From Same Cluster
        ↓
Compute Cosine Similarity
        ↓
Return Top Similar Songs
```

---

# 🎯 Objectives

* Understand Unsupervised Learning in a real-world application
* Implement K-Means Clustering on Spotify audio features
* Build a scalable recommendation engine
* Deploy an interactive ML application using Streamlit
* Create a portfolio-ready AIML project

---

# 📊 Dataset

Spotify Tracks Dataset

### Original Dataset

* 114,000+ songs
* 20 attributes

### Features Used

```python
danceability
energy
loudness
speechiness
acousticness
instrumentalness
liveness
valence
tempo
```

### Dataset After Cleaning

* ~81,000 songs

---

# 🧹 Data Preprocessing

### Data Cleaning

* Removed unnecessary columns
* Handled missing values
* Removed duplicate entries

### Feature Selection

Selected only audio features relevant for clustering.

### Feature Scaling

Used StandardScaler to normalize features.

Formula:

```text
z = (x - μ) / σ
```

This ensures all features contribute equally during clustering.

---

# 📈 Exploratory Data Analysis (EDA)

Performed:

* Missing Value Analysis
* Correlation Analysis
* Feature Distribution Analysis
* Cluster Distribution Analysis
* Audio Feature Relationship Study

### Key Observation

Energy and Loudness showed strong positive correlation, indicating louder songs tend to be more energetic.

---

# 🤖 Machine Learning Approach

## Step 1: K-Means Clustering

Songs were grouped based on similarity in audio characteristics.

### Why K-Means?

* Fast
* Scalable
* Easy to interpret
* Works well with standardized numerical features

---

## Step 2: Finding Optimal K

### Elbow Method

Used WCSS (Within Cluster Sum of Squares) to identify optimal number of clusters.

Optimal K:

```text
K = 7
```

---

## Step 3: Recommendation Engine

After clustering:

1. Find cluster of selected song
2. Retrieve songs from same cluster
3. Calculate cosine similarity
4. Return top recommendations

---

# 📐 Cosine Similarity

Used to measure similarity between songs.

Formula:

```text
cos(θ) = (A · B) / (||A|| ||B||)
```

### Why Cosine Similarity?

* Measures similarity in feature patterns
* Works well on high-dimensional data
* Commonly used in recommendation systems

---

# 🛠 Tech Stack

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-Learn
* K-Means Clustering
* Cosine Similarity

### Visualization

* Matplotlib
* Seaborn
* Plotly

### Deployment

* Streamlit

---

# 🎨 Features

### ✅ Song Search

Search songs instantly from 81K+ tracks.

### ✅ Cluster-Based Filtering

Recommendations generated from relevant clusters.

### ✅ Cosine Similarity Ranking

Ranks songs by similarity score.

### ✅ Audio Profile Visualization

Interactive radar chart displaying song characteristics.

### ✅ Cluster Insights

Visual representation of cluster distribution.

### ✅ Streamlit Dashboard

User-friendly web interface.

---

# 📷 Application Screenshots

### Home Page

(Add Screenshot Here)

### Recommendation Results

(Add Screenshot Here)

### Audio Profile Radar Chart

(Add Screenshot Here)

---

# 📊 Project Architecture

```text
Spotify Dataset
       ↓
Data Cleaning
       ↓
Feature Selection
       ↓
Standardization
       ↓
K-Means Clustering
       ↓
Cluster Assignment
       ↓
Cosine Similarity
       ↓
Recommendation Engine
       ↓
Streamlit Deployment
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into project directory:

```bash
cd Spotify-Hybrid-Recommender
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---

# 📂 Project Structure

```text
Spotify-Hybrid-Recommender/
│
├── app.py
├── spotify_tracks_with_clusters.csv
│
├── kmeans_model.pkl
├── model.ipynb
├── spotify-tracks-dataset-detailed.csv
│
├── screenshots/
├── EDA/
│
├── requirements.txt
│
└── README.md
```

---

# 🔥 Future Improvements

### Genre-Aware Recommendations

Combine:

```text
Cluster
+
Genre
+
Cosine Similarity
```

for better recommendations.

### Collaborative Filtering

Use user listening history.

### Deep Learning Embeddings

Learn song representations automatically.

### Spotify API Integration

Generate recommendations directly from Spotify playlists.

### Vector Database

Use FAISS or Pinecone for large-scale similarity search.

---

# 📚 Key Learnings

Through this project, I learned:

* Unsupervised Learning
* K-Means Clustering
* Feature Engineering
* Feature Scaling
* Recommendation Systems
* Cosine Similarity
* Streamlit Deployment
* End-to-End ML Project Development

---

# 👨‍💻 Author

**Anuj Kumar**

AIML Student | Machine Learning Enthusiast | Aspiring AI Engineer

### Connect With Me

* LinkedIn: *[(Click here...)](https://www.linkedin.com/in/anujkumar2005/)*
* GitHub: *[(Click here...)](https://github.com/anujkumar181609)*

---

# ⭐ If you found this project useful, consider giving it a star on GitHub!
