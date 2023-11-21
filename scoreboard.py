from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x= -280, y = 250)
        self.write(f"Level: {self.level}",align="left", font=FONT)
