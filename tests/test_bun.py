import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun

class TestBun:

    def test_bun_get_name(self):
        bun = Bun("white bun", 150)

        assert bun.get_name() == "white bun"


    def test_bun_get_price(self):
        bun = Bun("red bun", 200)

        assert bun.get_price() == 200