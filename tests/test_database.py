import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Тест проверяет метод available_buns()
def test_database_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3  # Проверяем количество доступных булочек
    assert buns[0].get_name() == "black bun"  # Проверяем первую булочку
    assert buns[1].get_price() == 200  # Проверяем цену второй булочки

# Тест проверяет метод available_ingredients()
def test_database_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6  # Проверяем общее количество ингредиентов
    assert ingredients[0].get_name() == "hot sauce"  # Проверяем первый соус
    assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE 