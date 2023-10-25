from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.show_lvl()

    def show_lvl(self):
        self.clear()
        self.write(f'level:{self.lvl}', align='left', font=FONT)

    def update_lvl(self):
        self.lvl += 1
        self.show_lvl()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER',align='center',font=FONT)