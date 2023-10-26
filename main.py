import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.car()
    car.move_cars()

    if player.ycor() > 280:
        player.reset()
        level.update_lvl()
        car.increase_speed_of_cars()

    for x in car.all_cars:
        if player.distance(x) < 20:
            game_is_on = False
            screen.clear()
            level.game_over()

    screen.update()

screen.exitonclick()
