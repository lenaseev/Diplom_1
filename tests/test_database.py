import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE

class TestDataBase:
    def test_database_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3  # Проверяем количество доступных булочек
        assert buns[0].get_name() == "black bun"  # Проверяем первую булочку
        assert buns[1].get_price() == 200  # Проверяем цену второй булочки

    def test_database_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6  # Проверяем общее количество ингредиентов
        assert ingredients[0].get_name() == "hot sauce"  # Проверяем первый соус
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE