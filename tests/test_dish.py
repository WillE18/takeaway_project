from lib.dish import *

def test_dish_title_initialised():
    dish = Dish("10 Chicken Wings", 
                "10 large BBQ flavoured chicken wings",
                ["mustard", "celery"],
                17.90)
    assert dish.title == "10 Chicken Wings"

def test_dish_description_initialised():
    dish = Dish("10 Chicken Wings", 
                "10 large BBQ flavoured chicken wings",
                ["mustard", "celery"],
                17.90)
    assert dish.description == "10 large BBQ flavoured chicken wings"

def test_dish_allergens_initialised():
    dish = Dish("10 Chicken Wings", 
                "10 large BBQ flavoured chicken wings",
                ["mustard", "celery"],
                17.90)
    assert dish.allergens == ["mustard", "celery"]

def test_dish_price_initialised():
    dish = Dish("10 Chicken Wings", 
                "10 large BBQ flavoured chicken wings",
                ["mustard", "celery"],
                17.90)
    assert dish.price == 17.90