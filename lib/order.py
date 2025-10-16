from datetime import datetime, timedelta


class Order:
    def __init__(self, basket, delivery_fee):
        self.basket = basket
        self.order_time = self._get_order_time()
        self.order_number = self._generate_order_number()
        self.delivery_fee = delivery_fee
    def _get_order_time(self):
        pass
    def _generate_order_number(self):
        pass
    def get_predicted_delivery_time(self):
        return self.order_time + timedelta(minutes=30)
    def get_total_price(self):
        return sum([dish.price for dish in self.basket.all_dishes()]) + self.delivery_fee