from unittest.mock import Mock
from lib.texter import *
from datetime import datetime

def test_texter_order_initialised():
    takeaway = Mock()
    takeaway.place_order.return_value = Mock()
    order = takeaway.place_order()
    texter = Texter(order)
    assert texter.order == order

def test_texter_send_text():
    takeaway = Mock()
    takeaway.place_order.return_value = Mock()
    order = takeaway.place_order()
    order.order_time = datetime(2025, 7, 21, 17, 30)
    order.get_predicted_delivery_time.return_value = datetime(2025, 7, 21, 18, 00)
    texter = Texter(order)
    assert texter.send() == "Thank you! Your order was placed and will be delivered before 18:00"