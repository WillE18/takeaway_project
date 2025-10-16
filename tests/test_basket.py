import pytest
from unittest.mock import Mock
from lib.basket import *

def test_empty_basket_initialised():
    takeaway = Mock()
    basket = Basket(takeaway)
    assert basket.all_dishes() == []

def test_add_dish_to_basket():
    dish1 = Mock()
    dish2 = Mock()
    dish3 = Mock()
    takeaway = Mock()
    takeaway.view_menu.return_value = [dish1, dish2, dish3]
    basket = Basket(takeaway)
    basket.add(dish1)
    assert basket.all_dishes() == [dish1]

def test_add_multiple_dishes_then_remove_dish():
    dish1 = Mock()
    dish2 = Mock()
    dish3 = Mock()
    takeaway = Mock()
    takeaway.view_menu.return_value = [dish1, dish2, dish3]
    basket = Basket(takeaway)
    basket.add(dish1)
    basket.add(dish2)
    basket.remove(dish1)
    assert basket.all_dishes() == [dish2]

def test_add_invalid_menu_item():
    dish1 = Mock()
    dish2 = Mock()
    takeaway = Mock()
    takeaway.view_menu.return_value = [dish1, dish2]
    dish3 = Mock()
    basket = Basket(takeaway)
    basket.add(dish1)
    basket.add(dish2)
    with pytest.raises(Exception) as err:
        basket.add(dish3)
    err_message = str(err.value)
    assert err_message == "Dish not in menu of Takeaway instance."
