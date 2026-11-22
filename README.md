# 🎬 Movie Recommender System

A content-based Movie Recommendation System built using Python, Machine Learning, and Streamlit. It recommends 5 similar movies based on a selected movie and displays their posters using the TMDB API.

### 🚀 Live Demo

🔗 **[Try the Movie Recommender System](https://movie-recommender-system-pree.streamlit.app/)**

### ✨ Features

- Search and select movies from the dataset.
- Get the top 5 similar movie recommendations.
- Display movie posters using the TMDB API.
- Simple and interactive Streamlit interface.
- Optimized similarity data for faster loading and cloud deployment.

### 🛠️ Tech Stack

- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Requests
- **Frontend:** Streamlit
- **API:** TMDB API
- **Deployment:** Streamlit Community Cloud

### 📊 Dataset

**TMDB 5000 Movie Dataset — Kaggle**

🔗 [Download Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

The dataset contains information about approximately 5,000 movies, including titles, genres, keywords, cast, crew, and overviews.

### ⚙️ How It Works

1. Movie data is processed to identify similarities between movies.
2. The recommendation system uses precomputed similarity information to find related movies.
3. The top 5 similar movies are selected.
4. Movie posters are fetched using the TMDB API.
5. Results are displayed through the Streamlit web application.

### ☁️ Deployment

The application is deployed on **Streamlit Community Cloud**, with optimized similarity data to reduce file size and improve deployment efficiency.

### 🙌 Acknowledgement

Movie metadata and posters are provided by [The Movie Database (TMDB)](https://www.themoviedb.org/).

This product uses the TMDB API but is not endorsed or certified by TMDB.

---

⭐ If you find this project useful, consider starring the repository!
