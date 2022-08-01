from unittest.mock import MagicMock

import pytest

from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre1 = Genre(id=1, name="Комедия")
    genre2 = Genre(id=2, name="Семейный")
    genre3 = Genre(id=3, name="Фантастика")

    genre_dao.get_one = MagicMock(return_value=genre1)
    genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()
    return genre_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre.id is not None
        assert genre is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0
        assert isinstance(genres, list)

    def test_create(self):
        new_genre = {
            'id': '4',
            'name': 'Драма'
        }
        genre = self.genre_service.create(new_genre)
        assert genre.id is not None

    def test_update(self):
        update_genre = {
            'id': 1,
            'name': 'Драма'
        }
        self.genre_service.update(update_genre)

    def test_delete(self):
        self.genre_service.delete(1)