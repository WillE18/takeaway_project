from unittest.mock import Mock
from lib.order import *

def test_order_basket_initialised():
    takeaway = Mock()
    dish1 = Mock()
    dish2 = Mock()
    basket = Mock()
    basket.view_all.return_value = [dish1, dish2]
    takeaway.place_order.return_value = Order(basket, 2.99)
    order = takeaway.place_order()
    assert order.basket == basket
    assert order.basket.view_all() == [dish1, dish2]

def test_get_total_order_price():
    takeaway = Mock()
    dish1 = Mock()
    dish2 = Mock()
    dish1.price = 17.99
    dish2.price = 12.99
    basket = Mock()
    basket.view_all.return_value = [dish1, dish2]
    takeaway.place_order.return_value = Order(basket, 2.99)
    order = takeaway.place_order()
    assert order.get_total_price() == 33.97