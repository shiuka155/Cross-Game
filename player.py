from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),self.new_y)
