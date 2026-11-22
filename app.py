
import pickle
import time
import requests
import streamlit as st

TMDB_API_KEY = st.secrets["TMDB_API_KEY"]


@st.cache_data(show_spinner=False)
def fetch_poster(movie_id: int) -> str | None:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": TMDB_API_KEY, "language": "en-US"}

    with requests.Session() as session:
        for attempt in range(2):
            try:
                response = session.get(
                    url, params=params, timeout=10
                )
                response.raise_for_status()

                poster_path = response.json().get("poster_path")

                if poster_path:
                    return f"https://image.tmdb.org/t/p/w500{poster_path}"

                return None

            except requests.RequestException:
                if attempt == 0:
                    time.sleep(0.5)

    return None


movies_df = pickle.load(open("movies.pkl", "rb"))
movie_titles = movies_df["title"].values
similarity = pickle.load(open("similarity.pkl", "rb"))


def recommend(movie):
    movie_idx = movies_df[
        movies_df["title"] == movie
    ].index[0]

    distances = similarity[movie_idx]

    movies_lists = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_lists:
        row = movies_df.iloc[i[0]]

        recommended_movies.append(row.title)
        recommended_posters.append(
            fetch_poster(int(row.movie_id))
        )

    return recommended_movies, recommended_posters


st.title("Movie Recommender System")

selected_movie = st.selectbox(
    "Search a Movie",
    options=movie_titles,
    index=None,
    placeholder="Search a Movie...",
)

if st.button(
    "Recommend",
    type="primary",
    use_container_width=True
):
    if selected_movie:
        st.success(
            f"Top recommendations for: {selected_movie}"
        )

        names, posters = recommend(selected_movie)

        cols = st.columns(5)

        for col, title, poster_url in zip(
            cols, names, posters
        ):
            with col:
                if poster_url:
                    try:
                        st.image(
                            poster_url,
                            use_container_width=True
                        )
                    except Exception:
                        try:
                            small_poster = poster_url.replace(
                                "/w500/", "/w342/"
                            )
                            st.image(
                                small_poster,
                                use_container_width=True
                            )
                        except Exception:
                            st.caption("No poster available")
                else:
                    st.caption("No poster available")

                st.markdown(f"**{title}**")

    else:
        st.warning("Please select a movie first.")
