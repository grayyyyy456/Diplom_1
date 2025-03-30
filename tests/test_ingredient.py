import pytest
from ingredient import Ingredient
from data import Data


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (Data.sauce, Data.sauce_name_1, Data.sauce_price_1),
        (Data.filling, Data.filling_name_1, Data.filling_price_1),
        (Data.sauce, Data.sauce_name_2, Data.sauce_price_2),
        (Data.filling, Data.filling_name_2, Data.filling_price_2)
    ])
    def test_initialization_type(self,ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (Data.sauce, Data.sauce_name_1, Data.sauce_price_1),
        (Data.filling, Data.filling_name_1, Data.filling_price_1),
        (Data.sauce, Data.sauce_name_2, Data.sauce_price_2),
        (Data.filling, Data.filling_name_2, Data.filling_price_2)
    ])
    def test_initialization_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (Data.sauce, Data.sauce_name_1, Data.sauce_price_1),
        (Data.filling, Data.filling_name_1, Data.filling_price_1),
        (Data.sauce, Data.sauce_name_2, Data.sauce_price_2),
        (Data.filling, Data.filling_name_2, Data.filling_price_2)
    ])
    def test_initialization_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
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
