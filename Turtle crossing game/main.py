from turtle import Screen 
from turtlebody import TurtleBody
from level import LevelNumber
from cars import Car
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle crossing game")
screen.tracer(0)

turtle = TurtleBody()
screen.listen()
screen.onkey(fun= turtle.go, key='Up')

level = LevelNumber()

car = Car()

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move()

    for cars in car.all_cars:
        if cars.distance(turtle) < 35:
            is_game_on = False
            level.gameover()

    if turtle.ycor() > 270:
        level.level_improve()
        car.level_up()
        turtle.refresh_position()

screen.exitonclick()