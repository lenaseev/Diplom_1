import pytest
from unittest.mock import MagicMock, patch
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
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


def test_set_buns(burger, bun):
    burger.set_buns(bun)
    assert burger.bun == bun


def test_add_ingredient(burger, ingredient_sauce):
    burger.add_ingredient(ingredient_sauce)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient_sauce


def test_remove_ingredient(burger, ingredient_sauce, ingredient_filling):
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    burger.remove_ingredient(0)
    assert len(burger.ingredients) == 1
    assert burger.ingredients[0] == ingredient_filling


def test_move_ingredient(burger, ingredient_sauce, ingredient_filling):
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    burger.move_ingredient(0, 1)
    assert burger.ingredients[0] == ingredient_filling
    assert burger.ingredients[1] == ingredient_sauce


def test_get_price(burger, bun, ingredient_sauce, ingredient_filling):
    burger.set_buns(bun)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    assert burger.get_price() == 100 * 2 + 100 + 200


def test_get_receipt(burger, bun, ingredient_sauce, ingredient_filling):
    burger.set_buns(bun)
    burger.add_ingredient(ingredient_sauce)
    burger.add_ingredient(ingredient_filling)
    receipt = burger.get_receipt()
    assert "(==== black bun ====)" in receipt
    assert "= sauce hot sauce =" in receipt
    assert "= filling cutlet =" in receipt
    assert "Price: 500" in receipt


@pytest.mark.parametrize(
    "ingredients, expected_price",
    [
        (["hot sauce", "cutlet"], 400),
        (["sour cream", "sausage"], 500),
        (["chili sauce", "dinosaur"], 600),
    ]
)
def test_burger_add_ingredient_parametrized(ingredients, expected_price):
    bun_mock = MagicMock(spec=Bun)
    bun_mock.get_price.return_value = 100
    bun_mock.get_name.return_value = "black bun"

    burger = Burger()
    burger.set_buns(bun_mock)

    for ingredient_name in ingredients:
        ingredient_mock = MagicMock(spec=Ingredient)
        ingredient_mock.get_name.return_value = ingredient_name
        ingredient_mock.get_price.return_value = 100
        ingredient_mock.get_type.return_value = INGREDIENT_TYPE_FILLING if ingredient_name != "hot sauce" else INGREDIENT_TYPE_SAUCE
        burger.add_ingredient(ingredient_mock)

    expected_total_price = bun_mock.get_price() * 2 + len(ingredients) * 100
    assert burger.get_price() == expected_total_price