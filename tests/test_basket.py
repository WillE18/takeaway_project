from unittest.mock import Mock
from lib.basket import *

def test_empty_basket_initialised():
    basket = Basket()
    assert basket.all_dishes() == []

def test_add_dish_to_basket():
    dish = Mock()
    basket = Basket()
    basket.add(dish)
    assert basket.all_dishes() == [dish]

def test_add_multiple_dishes_then_remove_dish():
    dish1 = Mock()
    dish2 = Mock()
    basket = Basket()
    basket.add(dish1)
    basket.add(dish2)
    basket.remove(dish1)
    assert basket.all_dishes() == [dish2]