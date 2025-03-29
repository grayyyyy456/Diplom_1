from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def test_database_initialization(self, database):
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6

    def test_database_buns(self, database):
        assert database.buns[0].get_name() == "black bun"
        assert database.buns[0].get_price() == 100
        assert database.buns[1].get_name() == "white bun"
        assert database.buns[1].get_price() == 200
        assert database.buns[2].get_name() == "red bun"
        assert database.buns[2].get_price() == 300

    def test_database_ingredients(self, database):
        assert database.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert database.ingredients[0].get_name() == "hot sauce"
        assert database.ingredients[0].get_price() == 100

        assert database.ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert database.ingredients[1].get_name() == "sour cream"
        assert database.ingredients[1].get_price() == 200

        assert database.ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert database.ingredients[2].get_name() == "chili sauce"
        assert database.ingredients[2].get_price() == 300

        assert database.ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert database.ingredients[3].get_name() == "cutlet"
        assert database.ingredients[3].get_price() == 100

        assert database.ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert database.ingredients[4].get_name() == "dinosaur"
        assert database.ingredients[4].get_price() == 200

        assert database.ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
        assert database.ingredients[5].get_name() == "sausage"
        assert database.ingredients[5].get_price() == 300

    def test_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[5].get_name() == "sausage"