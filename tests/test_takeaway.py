from unittest.mock import Mock
from lib.takeaway import *

def test_takeaway_places_order_and_gets_back_dishes():
    dish1 = Mock()
    dish2 = Mock()
    takeaway = Takeaway("Nandos", 2.99)
    basket = Mock()
    basket.all_dishes.return_value = [dish1, dish2]
    order = takeaway.place_order(basket)
    assert order.basket.all_dishes() == [dish1, dish2]

def test_takeaway_view_menu_initially_none():
    takeaway = Takeaway("Nandos", 2.99)
    assert takeaway.view_menu() == []

def test_takeaway_view_menu_after_adding_multiple():
    takeaway = Takeaway("Nandos", 2.99)
    dish1 = Mock()
    dish2 = Mock()
    takeaway.add_dish(dish1)
    takeaway.add_dish(dish2)
    assert takeaway.view_menu() == [dish1, dish2]

def test_takeaway_view_menu_after_adding_and_then_removing():
    takeaway = Takeaway("Nandos", 2.99)
    dish1 = Mock()
    dish2 = Mock()
    dish3 = Mock()
    takeaway.add_dish(dish1)
    takeaway.add_dish(dish2)
    takeaway.add_dish(dish3)
    takeaway.remove_dish(dish1)
    assert takeaway.view_menu() == [dish2, dish3]

def test_takeaway_view_order_history_initially_empty():
    takeaway = Takeaway("Nandos", 2.99)
    assert takeaway.view_order_history() == []

def test_takeaway_view_order_history_after_placing_multiple_orders():
    takeaway = Takeaway("Nandos", 2.99)
    basket = Mock()
    order1 = takeaway.place_order(basket)
    order2 = takeaway.place_order(basket)
    assert takeaway.view_order_history() == [order1, order2]