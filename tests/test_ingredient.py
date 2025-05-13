import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


def test_ingredient_get_name():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)

    assert ingredient.get_name() == "cutlet"


def test_ingredient_get_price():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 150)

    assert ingredient.get_price() == 150


def test_ingredient_get_type():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 250)

    assert ingredient.get_type() == INGREDIENT_TYPE_FILLING