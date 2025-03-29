from bun import Bun
import pytest

class TestBun:
    @pytest.mark.parametrize('name, price', [("верхняя булочка", 100),("нижняя булочка", 150)])
    def test_naming_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [("верхняя булочка", 40), ("нижняя булочка", 50)])
    def test_pricing_bun(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
