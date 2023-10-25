from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def car(self):
        if random.randint(1, 6) == 3:
            car = Turtle('square')
            car.penup()
            car.shapesize(1, 2)
            car.goto(300, random.randint(-260, 260))
            car.color(random.choice(COLORS))
            self.all_cars.append(car)

    def move_cars(self):
        for x in self.all_cars:
            x.backward(self.speed)

    def increase_speed_of_cars(self):
        self.speed += MOVE_INCREMENT
