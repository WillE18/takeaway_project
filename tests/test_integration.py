from lib.basket import *
from lib.dish import *
from lib.order import *
from lib.receipt_generator import *
from lib.takeaway import *
from lib.texter import *

def dont_run_yet_test_place_takeaway_order():
    takeaway = Takeaway("Nandos", 2.99)
    dish1 = Dish("10 Chicken Wings", 
                "10 large BBQ flavoured chicken wings",
                ["mustard", "celery"],
                17.90)
    dish2 = Dish("5 Chicken Wings", 
                "5 large BBQ flavoured chicken wings",
                ["mustard", "celery"],
                12.90)
    takeaway.add_dish(dish1)
    takeaway.add_dish(dish2)
    basket = Basket()
    basket.add(dish1)
    basket.add(dish2)
    takeaway.place_order(basket)