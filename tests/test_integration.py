from lib.basket import *
from lib.dish import *
from lib.order import *
from lib.receipt_generator import *
from lib.takeaway import *
from lib.texter import *

dish1 = Dish("10 Chicken Wings", 
            "10 large BBQ flavoured chicken wings",
            ["mustard", "celery"],
            17.90)
dish2 = Dish("5 Chicken Wings", 
            "5 large BBQ flavoured chicken wings",
            ["mustard", "celery"],
            12.90)
dish3 = Dish("3 Chicken Wings", 
            "3 large BBQ flavoured chicken wings",
            ["mustard", "celery"],
            17.90)

def test_add_takeaway_dish():
    takeaway = Takeaway("Nandos", 2.99)
    takeaway.add_dish(dish1)
    takeaway.add_dish(dish2)
    assert takeaway.menu == [dish1, dish2]

def test_remove_takeaway_dish():
    takeaway = Takeaway("Nandos", 2.99)
    takeaway.add_dish(dish1)
    takeaway.add_dish(dish2)
    takeaway.remove_dish(dish1)
    assert takeaway.menu == [dish2]


def test_view_menu_after_adding_multiple_items():
    takeaway = Takeaway("Nandos", 2.99)
    takeaway.add_dish(dish1)
    takeaway.add_dish(dish2)
    assert takeaway.menu == [dish1, dish2]

def test_place_takeaway_order():
    takeaway = Takeaway("Nandos", 2.99)
    takeaway.add_dish(dish1)
    takeaway.add_dish(dish2)
    basket = Basket(takeaway)
    basket.add(dish1)
    basket.add(dish2)
    order = takeaway.place_order(basket)
    assert takeaway.order_history == [order]

def test_order_history_after_placing_multiple_orders():
    takeaway = Takeaway("Nandos", 2.99)
    takeaway.add_dish(dish1)
    takeaway.add_dish(dish2)
    takeaway.add_dish(dish3)
    basket1 = Basket(takeaway)
    basket1.add(dish1)
    basket1.add(dish2)
    order1 = takeaway.place_order(basket1)
    basket2 = Basket(takeaway)
    basket2.add(dish2)
    basket2.add(dish3)
    order2 = takeaway.place_order(basket2)
    assert takeaway.order_history == [order1, order2]

