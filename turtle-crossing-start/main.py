import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car =CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move()

    # #collision with car
    for cars in car.all_cars:
        if cars.distance(player)<20:
            score.game_over()
            game_is_on= False


    # reaching the other end
    if player.finish_line():
        player.start_position()
        car.level_up()
        score.levelup()

screen.exitonclick()