import pandas as pd
import pickle
import difflib

# Load pre-trained models safely
try:
    movies_dict = pickle.load(open("models/movies_list.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open("models/similarity.pkl", "rb"))
except FileNotFoundError:
    print("Warning: Model files not found. Please run 'python src/train.py' first.")
    movies = pd.DataFrame(columns=['title', 'title_lower'])
    similarity = []

def recommend(movie):
    if movies.empty:
        return ["System updating. Please try again later."]

    movie = movie.lower()
    movies['title_lower'] = movies['title'].str.lower()

    # Typo Tolerance using fuzzy matching
    close_matches = difflib.get_close_matches(movie, movies['title_lower'].values, n=1, cutoff=0.6)
    
    if not close_matches:
        # Graceful cold-start fallback
        return ["Movie not found! Check spelling or try a popular movie like 'Avatar'."]
        
    matched_movie = close_matches[0]
    movie_index = movies[movies['title_lower'] == matched_movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(list(enumerate(distances)),
                        reverse=True,
                        key=lambda x:x[1])[1:6]

    recommended_movies = []
    
    # If there was a typo, optionally append what it was autocorrected to
    if matched_movie != movie:
        recommended_movies.append(f"Showing results for: {movies.iloc[movie_index].title}")
        # Only take the next 4 to keep it at 5 lines
        for i in movie_list[:4]: 
            recommended_movies.append(movies.iloc[i[0]].title)
    else:
        for i in movie_list:
            recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

def get_movie_list():
    if movies.empty:
        return []
    return movies['title'].values.tolist()