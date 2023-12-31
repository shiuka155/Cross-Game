from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.reset_position()
        self.my_speed = STARTING_MOVE_DISTANCE



    def speed_up(self):
        self.my_speed += MOVE_INCREMENT


    def reset_position(self):
        self.random_y_respawn = random.randrange(-300, 300, 30)
        self.random_x_respawn = random.randrange(300,500, 30)
        self.goto(self.random_x_respawn, self.random_y_respawn)

    def move(self):
        new_x = self.xcor() - self.my_speed
        self.goto(new_x, self.ycor())

