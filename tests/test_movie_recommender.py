"""This is the logging and unittesting code for the MovieRecommendation class"""

import os
import sys
sys.path.append(os.getcwd())
import unittest
import logging
from recommendation_system.src.movie_recommender import MovieRecommendation


def create_logger() -> logging.Logger:
    """This function creates and returns a custom logger"""
    if not os.path.exists(os.path.join(os.getcwd(), 'logs')):
        os.makedirs(os.path.join(os.getcwd(), 'logs'))

    logger = logging.getLogger(name='test_movie_recommender')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # Console logging handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    # File logging handler
    file_handler = logging.FileHandler('logs/test_movie_recommender_logs.log')
    file_handler.setFormatter(formatter)
    # Adding handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


class TestMovieRecommendation(unittest.TestCase):
    """The class for unit testing all methods of the MovieRecommendation class"""

    @classmethod
    def setUpClass(cls):
        cls.logger = create_logger()
        cls.logger.info('=' * 50)
        cls.logger.info('Starting TestMovieRecommendation class')
        cls.movie_recommendation = MovieRecommendation()

    def test_get_random_movies(self):
        """Unit-test for get_random_movies method"""
        result = self.movie_recommendation.get_random_movies()

        # Assertions
        self.assertEqual(len(result), 6)
        self.assertTrue(all(isinstance(movie['id'], int) for movie in result))
        self.assertTrue(all(isinstance(movie['title'], str) for movie in result))
        self.assertTrue(all(isinstance(movie['poster_path'], str) for movie in result))
        self.logger.info('All get_random_movies method tests passed')

    def test_get_recommended_movies(self):
        """Unit-test for get_recommended_movies method"""
        result = self.movie_recommendation.get_recommended_movies('Iron Man')
        # Assertions
        self.assertEqual(len(result), 6)
        self.assertTrue(all(isinstance(movie['id'], int) for movie in result))
        self.assertTrue(all(isinstance(movie['title'], str) for movie in result))
        self.assertTrue(all(isinstance(movie['poster_path'], str) for movie in result))
        logging.info('All get_recommended_movies method tests passed')


if __name__ == '__main__':
    unittest.main()
