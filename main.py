"""MovieRecommendation Flask project documentation"""
from flask import Flask, render_template, request, redirect
from recommendation_system.src.movie_recommender import MovieRecommendation

app = Flask(__name__, template_folder='./recommendation_system/templates')
app_obj = MovieRecommendation()
"""This is a Flask application"""


# Route for home page
@app.route('/')
def index():
    """Home page"""
    random_movies = app_obj.get_random_movies()
    return render_template('/index.html', movie_data=random_movies)


# Route for recommendation page
@app.route('/recommendation', methods=['POST'])
def recommendation():
    """Recommendation page"""
    # Get user input and perform recommendation logic
    # Dummy example: Just pass a list of recommended movies
    recommended_movies = [{}]
    if request.method == 'POST':
        movie_title = str(request.form['movie_title']).title()
        recommended_movies = app_obj.get_recommended_movies(movie_title)
        if len(recommended_movies) == 0:
            recommended_movies.extend(app_obj.get_random_movies())
            return redirect('/')
    return render_template('recommend.html', movie_data=recommended_movies)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
