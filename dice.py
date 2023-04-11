# imports
import random


# creating a class to represent the die.
class Die:
    def __init__(self):
        self.value = 0

    def rroll(self):
        """
        Rolls the die.
        """
        self.value = random.randint(1, 6)

    def getText(self):
        return f"{self.value}"
