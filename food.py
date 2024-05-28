import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        """Food class constructor."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a new random location."""
        self.goto(x = random.randint(-280, 280), y = random.randint(-280, 280))