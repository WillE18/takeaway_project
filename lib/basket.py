class Basket:
    def __init__(self):
        self._dishes = []
    def add(self, dish):
        self._dishes.append(dish)
    def remove(self, dish):
        self._dishes.remove(dish)
    def view_all(self):
        return self._dishes