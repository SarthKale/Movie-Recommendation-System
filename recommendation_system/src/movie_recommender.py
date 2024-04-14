"""Importing the required modules"""
import pickle
import time
import random
import warnings
import pandas as pd
warnings.filterwarnings("ignore",category=FutureWarning)


class MovieRecommendation:
    """MovieRecommendation class documentation"""

    def __init__(self) -> None:
        """Initialize a MovieRecommendation"""
        self.poster_prefix = 'https://image.tmdb.org/t/p/w500'
        self.file_path = 'recommendation_system/data/recommendations_data.pkl'
        self.movie_data = self._read_data()

    def _read_data(self) -> pd.DataFrame:
        """Read the pickle file and return the data"""
        file = open(self.file_path, 'rb')
        data = pickle.load(file=file)
        file.close()
        return pd.DataFrame(data)

    def get_random_movies(self) -> list[dict]:
        """Return a list of random movies title and other details"""
        random.seed(time.time())
        random_movies_index = random.sample(self.movie_data['id'].unique().tolist(), 6)
        random_movies = self.movie_data[(self.movie_data['id'].isin(random_movies_index))]
        random_movies.loc[:, 'poster_path'] = random_movies['poster_path'].apply(
            lambda x: self.poster_prefix + str(x))
        return random_movies.to_dict(orient='records')

    def get_recommended_movies(self, movie_title) -> list[dict]:
        """Return a list of recommendations"""
        if movie_title not in self.movie_data['title'].unique():
            return [{}]
        # movie_id = self.movie_data[(self.movie_data['title'] == movie_title)]['id'].tolist()[0]
        recommend_indices = list(self.movie_data[(self.movie_data['title'] == movie_title)][
            'recommendations'].tolist()[0])
        recommended_movies = self.movie_data[(self.movie_data['id'].isin(recommend_indices[:6]))]
        recommended_movies.loc[:, 'poster_path'] = recommended_movies['poster_path'].apply(
            lambda x: self.poster_prefix + str(x))
        recommended_movies = recommended_movies.to_dict(orient='records')

        recommended_movies = [movie for movie in recommended_movies if movie['title'] == movie_title
                    ] + [movie for movie in recommended_movies if movie['title'] != movie_title]
        return recommended_movies
