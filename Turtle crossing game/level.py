from turtle import Turtle

ALING = "center"
FONT = ('Impact', 14, 'normal')

class LevelNumber(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-240, 250) 
        self.level = 1
        self.showlevel()

    def showlevel(self):
        self.write(f"Level:{self.level}", align=ALING, font=FONT)

    def level_improve(self):
        self.level += 1
        self.clear()
        self.showlevel()

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", align=ALING, font=FONT)