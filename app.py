import pickle
import streamlit as st
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Load the movie data
movies_df = pickle.load(open('movies.pkl', 'rb'))

st.title('Movie Recommender System')

# Assuming movies.pkl contains a DataFrame
movies_list = movies_df['title'].values
selected_name = st.selectbox('Click below to Choose your Movie', movies_list)

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
    return recommended_movies_name,recommended_movie_posters

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_name)
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
