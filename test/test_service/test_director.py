from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director1 = Director(id=1, name="Квентин Тарантино")
    director2 = Director(id=2, name="Владимир Вайншток")
    director3 = Director(id=3, name="Джеки Чан")

    director_dao.get_one = MagicMock(return_value=director1)
    director_dao.get_all = MagicMock(return_value=[director1, director2, director3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


class TestUserService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director.id is not None
        assert director is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0
        assert isinstance(directors, list)

    def test_create(self):
        new_director = {
            'id': '4',
            'name': 'Стивен Спилберг'
        }
        director = self.director_service.create(new_director)
        assert director.id is not None

    def test_update(self):
        update_director = {
            'id': 1,
            'name': 'Стивен Спилберг'
        }
        self.director_service.update(update_director)

    def test_delete(self):
        self.director_service.delete(1)
