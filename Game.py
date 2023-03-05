import random


class Game:
    def __init__(self, car, choice, switch):
        self.car = car
        self.choice = choice
        self.switch = switch

    def win(self):
        if self.choice == self.car and self.switch:
            return False
        elif self.choice == self.car and not self.switch:
            return True
        elif self.choice != self.car and self.switch:
            return True
        elif self.choice != self.car and not self.switch:
            return False
