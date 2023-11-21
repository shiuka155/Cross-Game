import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

# create turtle
turtle = Player()

# create response on key
screen.listen()
screen.onkey(turtle.move_up, "Up")


# create the scoreboard level
scoreboard = Scoreboard()

# create car
cars = [CarManager() for _ in range(10)]

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    # if turtle.ycor() >= 290:
    #     game_is_on = False
    #     print("Done")
    for car in cars:
        car.move()
        if car.xcor() < - 300:
            car.reset_position()

