class Basket:
    def __init__(self, takeaway):
        self._dishes = []
        self.takeaway = takeaway
    def add(self, dish):
        if dish not in self.takeaway.view_menu():
            raise Exception("Dish not in menu of Takeaway instance.")
        self._dishes.append(dish)
    def remove(self, dish):
        self._dishes.remove(dish)
    def all_dishes(self):
        return self._dishes