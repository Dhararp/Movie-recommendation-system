import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

def train_model():
    print("Loading datasets...")
    movies = pd.read_csv("dataset/tmdb_5000_movies.csv")
    credits = pd.read_csv("dataset/tmdb_5000_credits.csv")

    movies = movies.merge(credits, on="title")
    movies = movies[['title', 'genres', 'keywords', 'overview']]
    movies = movies.fillna('')

    # Combine features into a single tags column
    movies['tags'] = movies['genres'] + " " + movies['keywords'] + " " + movies['overview']

    print("Stemming text data (this may take a moment)...")
    ps = PorterStemmer()
    
    def stem(text):
        return " ".join([ps.stem(word) for word in text.split()])
        
    movies['tags'] = movies['tags'].apply(stem)

    print("Vectorizing using TF-IDF...")
    # Replacing CountVectorizer with TfidfVectorizer to heavily weight unique features
    tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
    vector = tfidf.fit_transform(movies['tags']).toarray()

    print("Computing Cosine Similarity...")
    similarity = cosine_similarity(vector)

    print("Saving models...")
    os.makedirs('models', exist_ok=True)
    
    # Saving dataframe as a dict to avoid cross-version Pickling issues with Pandas
    pickle.dump(movies.to_dict(), open('models/movies_list.pkl', 'wb'))
    pickle.dump(similarity, open('models/similarity.pkl', 'wb'))

    print("Training complete! Models saved to the 'models/' directory.")

if __name__ == "__main__":
    train_model()
