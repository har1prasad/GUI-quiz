from turtle import Turtle, colormode
import random

colormode(255)
SPEED = 10
LEVEL = 1

def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

class Car():
    def __init__(self):
        self.all_cars = []
        self.carspeed = 10
        self.level_number = 5

    def create_cars(self):
        if  random.randint(1, self.level_number) == self.level_number:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(randomcolor())
            new_car.penup()
            new_car.shapesize(stretch_wid=1.5, stretch_len=3)
            new_car.setheading(180)
            new_car.goto(300, random.randint(-235, 235))
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars: 
            cars.forward(self.carspeed)

    def level_up(self):
        self.level_number -= LEVEL
        self.carspeed += SPEED

