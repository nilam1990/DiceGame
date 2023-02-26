import random


class Die:
    """ each player has Die instance. Die has value as an instance attribute initially it has None
    value because we haven't rolled die yet """
    def __init__(self):
        self._value = None

    @property
    def value(self):
        """ here we define property(getter) for value attribute to get the value of Die """
        return self._value

    def roll(self):
        """ Die has roll method to rolled it. so that we get new random value when we rolled it"""
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value

