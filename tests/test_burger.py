from unittest.mock import Mock
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    def test_set_buns(self, setup_burger):
        assert setup_burger.bun.get_name() == "булочка"

    def test_add_ingredient(self, setup_burger):
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = "котлета"
        mock_ingredient.get_price.return_value = 500
        setup_burger.add_ingredient(mock_ingredient)
        assert setup_burger.ingredients[0].get_name() == "котлета"

    def test_remove_ingredient(self, setup_burger):
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "котлета"
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "соус"
        setup_burger.add_ingredient(mock_ingredient1)
        setup_burger.add_ingredient(mock_ingredient2)
        setup_burger.remove_ingredient(0)
        assert setup_burger.ingredients[0].get_name() == "соус"

    def test_move_ingredient(self, setup_burger):
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "котлета"
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "соус"
        setup_burger.add_ingredient(mock_ingredient1)
        setup_burger.add_ingredient(mock_ingredient2)
        setup_burger.move_ingredient(0, 1)
        assert setup_burger.ingredients[0].get_name() == "соус"
        assert setup_burger.ingredients[1].get_name() == "котлета"

    def test_get_price(self, setup_burger):
        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 500
        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 10
        setup_burger.add_ingredient(mock_ingredient1)
        setup_burger.add_ingredient(mock_ingredient2)
        expected_price = setup_burger.bun.get_price() * 2 + mock_ingredient1.get_price() + mock_ingredient2.get_price()
        assert setup_burger.get_price() == expected_price

    def test_get_receipt(self, setup_burger):
        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = "котлета"
        mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient1.get_price.return_value = 500
        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = "соус"
        mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient2.get_price.return_value = 10
        setup_burger.add_ingredient(mock_ingredient1)
        setup_burger.add_ingredient(mock_ingredient2)
        expected_receipt = (
            f'(==== {setup_burger.bun.get_name()} ====)\n'
            f'= filling котлета =\n'
            f'= sauce соус =\n'
            f'(==== {setup_burger.bun.get_name()} ====)\n'
            f'\n'
            f'Price: {setup_burger.get_price()}'
        )
        assert setup_burger.get_receipt() == expected_receipt