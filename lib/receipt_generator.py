class ReceiptGenerator:
    def __init__(self, order):
        self.order = order
    def receiptify(self):
        return {
            "time_of_order": self.order.order_time,
            "order_number": self.order.order_number,
            "dishes": self.order.basket.all_dishes(),
            "total_price": self.order.get_total_price()
        }