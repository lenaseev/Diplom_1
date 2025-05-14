import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun():
    return Bun("black bun", 100)


@pytest.fixture
def ingredient_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)


@pytest.fixture
def ingredient_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)
