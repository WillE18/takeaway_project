class Texter:
    def __init__(self, order):
        self.order = order
    def send(self):
        delivery_time = self.order.get_predicted_delivery_time().time().strftime("%H:%M")
        message = f"Thank you! Your order was placed and will be delivered before {delivery_time}"
        return message
