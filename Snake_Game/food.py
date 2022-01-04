from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # The shapesize function increases/decreases the length and width of the turtle
        # In this case, it reduces the size of the turtle to half.
        self.shapesize(0.5, 0.5)
        self.color("Red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-290, 290)  # 290 because giving 10 units of space for the turtle body
        random_y = random.randint(-290, 290)  # 290 because giving 10 units of space for the turtle body
        self.goto(random_x, random_y)