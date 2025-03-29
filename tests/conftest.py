import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))
import pytest
from unittest.mock import Mock
from burger import Burger
from database import Database


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "булочка"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def setup_burger(burger, mock_bun):
    burger.set_buns(mock_bun)
    return burger

@pytest.fixture
def database():
    return Database()