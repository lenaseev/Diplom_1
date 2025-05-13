import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun


def test_bun_get_name():
    bun = Bun("white bun", 150)

    assert bun.get_name() == "white bun"


def test_bun_get_price():
    bun = Bun("red bun", 200)

    assert bun.get_price() == 200