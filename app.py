from flask import Flask, render_template, request
from model import recommend, get_movie_titles

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    movie_data = []
    if request.method == 'POST':
        movie_name = request.form['movie']
        movie_data = recommend(movie_name)
    movie_list = get_movie_titles()
    return render_template('index.html', movie=movie_data, movie_list=movie_list)

if __name__ == '__main__':
    app.run(debug=True)
