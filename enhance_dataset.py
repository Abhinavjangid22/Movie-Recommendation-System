import pandas as pd
import ast

movies = pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")
movies = movies.merge(credits, on='title')

def get_top_cast(cast_str):
    try:
        cast = ast.literal_eval(cast_str)
        return [actor['name'] for actor in cast[:3]]
    except:
        return []

def get_music_director(crew_str):
    try:
        crew = ast.literal_eval(crew_str)
        for member in crew:
            if member['job'] == 'Original Music Composer':
                return member['name']
        return ""
    except:
        return ""

df = movies[['title', 'id', 'overview', 'cast', 'crew']].copy()
df['cast'] = df['cast'].apply(get_top_cast)
df['music_director'] = df['crew'].apply(get_music_director)
df.drop(columns=['crew'], inplace=True)

df.to_csv("enhanced_movies.csv", index=False)
print("✅ enhanced_movies.csv is ready (without posters)")
