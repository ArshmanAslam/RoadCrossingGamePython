from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('black')
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(STARTING_POSITION)
