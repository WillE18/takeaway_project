from lib.order import *

class Takeaway:
    def __init__(self, name, delivery_fee):
        self.name = name
        self.delivery_fee = delivery_fee
        self.menu = []
        self.order_history = []
    def place_order(self, basket):
        order = Order(basket, self.delivery_fee)
        self.order_history.append(order)
        return order
    def view_menu(self):
        return self.menu
    def add_dish(self, dish):
        self.menu.append(dish)
    def remove_dish(self, dish):
        self.menu.remove(dish)
    def view_order_history(self):
        return self.order_history