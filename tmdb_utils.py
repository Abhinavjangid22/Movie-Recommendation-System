import requests

API_KEY = "d1b6a6fa6a2b1c1d9edc755f996e76b3"

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&append_to_response=credits"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'title': data.get('title'),
            'overview': data.get('overview'),
            'poster_url': f"https://image.tmdb.org/t/p/w500{data.get('poster_path')}" if data.get('poster_path') else None,
            'release_date': data.get('release_date'),
            'rating': data.get('vote_average'),
            'cast': [actor['name'] for actor in data['credits']['cast'][:5]],
            'director': next((crew['name'] for crew in data['credits']['crew'] if crew['job'] == 'Director'), None),
            'music': next((crew['name'] for crew in data['credits']['crew'] if crew['department'] == 'Sound'), None),
        }
    return None
