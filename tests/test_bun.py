from bun import Bun
import pytest
from data import Data

class TestBun:
    @pytest.mark.parametrize('name, price', [(Data.name_bun_1 , Data.price_bun_1),(Data.name_bun_2, Data.price_bun_2)])
    def test_naming_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [(Data.name_bun_1, Data.price_bun_1), (Data.name_bun_2, Data.price_bun_2)])
    def test_pricing_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
