from unittest.mock import *
from lib.receipt_generator import *

def test_receipt_generator_initialises_order():
    takeaway = Mock()
    takeaway.place_order.return_value = Mock()
    dish1 = Mock()
    dish2 = Mock()
    basket = Mock()
    basket.all_dishes.return_value = [dish1, dish2]
    order = takeaway.place_order()
    order.basket = basket
    receipter = ReceiptGenerator(order)
    assert receipter.order == order

def test_receipt_generator_creates_receipt():
    dish1 = Mock("10 Chicken Wings", 
                "10 large BBQ flavoured chicken wings",
                ["mustard", "celery"],
                17.90)
    dish2 = Mock("1/2 Chicken", 
                "1/2 BBQ flavoured chicken",
                ["mustard", "celery"],
                16.50)
    takeaway = Mock()
    takeaway.place_order.return_value = Mock()
    basket = Mock()
    basket.all_dishes.return_value = [dish1, dish2]
    order = takeaway.place_order()
    order.basket = basket
    order.order_time = "12/03/2026 17:46"
    order.order_number = 245798
    order.delivery_fee = 2.99
    order.get_total_price.return_value = 37.39
    receipter = ReceiptGenerator(order)
    receipt = receipter.receiptify()
    assert receipt["time_of_order"] == "12/03/2026 17:46"
    assert receipt["order_number"] == 245798
    assert receipt["dishes"] == basket.all_dishes()
    assert receipt["total_price"] == order.get_total_price()