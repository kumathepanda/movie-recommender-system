import pickle
import streamlit as st
import pandas as pd
import requests
import gdown

# Function to fetch movie posters
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    return "https://via.placeholder.com/500"  # Placeholder if no poster is available

# Function to download and cache files from Google Drive
@st.cache_data
def download_and_load_file(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_path, quiet=True)
    with open(output_path, "rb") as file:
        return pickle.load(file)

# Google Drive File IDs
similarity_file_id = "1cMMKHFtuXAUq2Qbw8oxm8SO55mhktp1c"  # Replace with the actual file ID
movies_file_id = "1SrQyHaUq-aJOxBFz5PpEd7MWjOpDqp6U"       # Replace with the actual file ID

# Load the similarity matrix and movies DataFrame only once
similarity = download_and_load_file(similarity_file_id, "similarity.pkl")
movies_df = download_and_load_file(movies_file_id, "movies.pkl")

# Streamlit app
st.title('Movie Recommender System')

# Assuming movies.pkl contains a DataFrame
movies_list = movies_df['title'].values
selected_name = st.selectbox('Click below to Choose your Movie', movies_list)

# Recommendation function
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_name = []
    recommended_movie_posters = []
    for i in movie_indices:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies_df.iloc[i[0]]['title'])
    return recommended_movies_name, recommended_movie_posters

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
