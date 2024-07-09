from turtle import Turtle

class TurtleBody(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0,-270)

    def refresh_position(self):
        self.goto(0,-270)

    def go(self):
        self.forward(20)
