import os
import pandas as pd
import requests
from dotenv import load_dotenv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")

if not API_KEY:
    raise ValueError("❌ TMDB_API_KEY not found. Please make sure it's set in the .env file.")

# Load dataset
df = pd.read_csv("enhanced_movies.csv")

# Combine features into a single tag field
df['tags'] = (
    df['overview'].fillna('') + ' ' +
    df['cast'].apply(lambda x: ' '.join(eval(x)) if isinstance(x, str) else '') + ' ' +
    df['music_director'].fillna('')
)

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(df['tags']).toarray()
similarity = cosine_similarity(vectors)

def fetch_poster(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    try:
        response = requests.get(url, verify=False)
        data = response.json()
        if data['results']:
            poster_path = data['results'][0].get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"


def fetch_overview(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
    try:
        response = requests.get(url, verify=False)
        data = response.json()
        if data['results']:
            return data['results'][0].get('overview', '')
    except:
        pass
    return ''


def recommend(movie):
    movie = movie.lower().strip()

    # Try exact match
    matched = df[df['title'].str.lower() == movie]

    # If no exact match, try partial match
    if matched.empty:
        matched = df[df['title'].str.lower().str.contains(movie)]

    if matched.empty:
        return []

    idx = matched.index[0]
    distances = list(enumerate(similarity[idx]))
    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:10]

    data = []
    for i in movies_list:
        m = df.iloc[i[0]]
        data.append({
            'title': m['title'],
            'overview': fetch_overview(m['title']) or m['overview'],
            'cast': ', '.join(eval(m['cast'])) if isinstance(m['cast'], str) else '',
            'music': m['music_director'],
            'poster': fetch_poster(m['title'])
        })
    return data

def get_movie_titles():
    return df['title'].tolist()
