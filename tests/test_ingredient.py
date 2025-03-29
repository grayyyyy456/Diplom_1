import pytest
from ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("sauce", "hot sauce", 100.0),
        ("filling", "cutlet", 150.0),
        ("sauce", "chili sauce", 300.0),
        ("filling", "sausage", 200.0)
    ])
    def test_initialization(self,ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_price(self):
        ingredient = Ingredient("filling", "cutlet", 150.0)
        assert ingredient.get_price() == 150.0

    def test_name(self):
        ingredient = Ingredient("filling", "sausage", 200.0)
        assert ingredient.get_name() == "sausage"

    def test_type(self):
        ingredient = Ingredient("sauce", "sour cream", 50.0)
        assert ingredient.get_type() == "sauce"
