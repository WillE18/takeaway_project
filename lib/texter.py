

class Texter:
    def __init__(self, order, text_sender):
        self.order = order
        self.text_sender = text_sender
    def send(self):
        delivery_time = self.order.get_predicted_delivery_time().time().strftime("%H:%M")
        message = f"Thank you! Your order was placed and will be delivered before {delivery_time}"
        return message
