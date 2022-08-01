from unittest.mock import MagicMock

import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(
        id=1,
        title="Бурлеск",
        description='test',
        trailer='test',
        year=2010,
        rating='test',
        genre_id=18,
        director_id=5,
    )
    movie2 = Movie(
        id=2,
        title="Чикаго",
        description='test',
        trailer='test',
        year=2002,
        rating='test',
        genre_id=18,
        director_id=6,
    )
    movie3 = Movie(
        id=3,
        title="Упс... Приплыли!",
        description='test',
        trailer='test',
        year=2020,
        rating='test',
        genre_id=16,
        director_id=19,
    )

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie.id is not None
        assert movie is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0
        assert isinstance(movies, list)

    def test_create(self):
        new_movie = {
            'id': 4,
            'title': 'Ирония судьбы',
            'description': 'test',
            'trailer': 'test',
            'year': 1999,
            'rating': 'test',
            'genre_id': 20,
            'director_id': 30,
        }
        movie = self.movie_service.create(new_movie)
        assert movie.id is not None

    def test_update(self):
        update_movie = {
            'id': 1,
            'title': 'Ирония судьбы',
            'description': 'test',
            'trailer': 'test',
            'year': 1999,
            'rating': 'test',
            'genre_id': 20,
            'director_id': 30,
        }
        self.movie_service.update(update_movie)

    def test_delete(self):
        self.movie_service.delete(1)
