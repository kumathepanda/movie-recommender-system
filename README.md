# Movie Recommender System

This project is a content-based movie recommender system that suggests movies similar to a user's choice. The recommendations are based on movie metadata like genres, keywords, cast, and crew.

## Deployed App

You can use the deployed application here: [https://movie-recommender-system-panda.streamlit.app/](https://movie-recommender-system-panda.streamlit.app/)

## How It Works

The recommender system is built using a content-based filtering approach. Here's a breakdown of the steps involved:

1.  **Data Collection**: The system uses two datasets from The Movie Database (TMDB): `tmdb_5000_credits.csv` and `tmdb_5000_movies.csv`.
2.  **Data Preprocessing**:
    * The two datasets are merged into a single dataframe.
    * The relevant columns for building the model are selected: `movie_id`, `genres`, `keywords`, `title`, `overview`, `cast`, and `crew`.
    * Data cleaning is performed, which includes handling missing values and removing duplicates.
    * The `genres`, `keywords`, `cast`, and `crew` columns, which are in a JSON-like string format, are parsed to extract the relevant names. For the cast, only the top 3 actors are considered, and for the crew, only the director's name is extracted.
3.  **Feature Engineering**:
    * A `tags` column is created by combining the `overview`, `genres`, `keywords`, `cast`, and `crew` columns. This creates a single text corpus for each movie that describes its content.
    * The text in the `tags` column is converted to lowercase and stemmed to reduce it to its root form.
4.  **Vectorization**:
    * The textual data in the `tags` column is converted into numerical vectors using the `CountVectorizer` from scikit-learn. This process, also known as vectorization, creates a vocabulary of the 5000 most frequent words and represents each movie as a vector of word counts.
5.  **Similarity Calculation**:
    * The cosine similarity between the vectors of all movies is calculated. Cosine similarity measures the cosine of the angle between two vectors, which indicates how similar they are. A higher cosine similarity score means the movies are more similar in content.
6.  **Recommendation**:
    * When a user selects a movie, the system finds the index of that movie in the dataset.
    * It then retrieves the similarity scores of that movie with all other movies.
    * The movies are sorted based on their similarity scores in descending order.
    * The top 5 most similar movies are recommended to the user.

## Technologies Used

* **Python**: The core programming language used for the project.
* **Pandas**: For data manipulation and analysis.
* **NumPy**: For numerical operations.
* **scikit-learn**: For implementing the CountVectorizer and calculating cosine similarity.
* **NLTK**: For natural language processing tasks like stemming.
* **Streamlit**: For creating and deploying the web application.
* **Requests**: For making API calls to fetch movie posters.
* **gdown**: To download files from Google Drive.

## How to Use the App

1.  Visit the app at [https://movie-recommender-system-panda.streamlit.app/](https://movie-recommender-system-panda.streamlit.app/).
2.  Select a movie from the dropdown menu.
3.  Click the "Show Recommendation" button.
4.  The app will display the posters and titles of the 5 recommended movies.
