FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.goto(-280,260)
        self.write(f"Level: {self.level}",align = "left",font = FONT)

    def increase(self):
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Courier", 24, "bold"))
