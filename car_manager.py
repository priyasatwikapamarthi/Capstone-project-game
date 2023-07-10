COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager :
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE



    def move_car(self):
        for car in self.cars :
            car.backward(self.car_speed)

    def generate_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1 :
            tim = Turtle("square")
            tim.shapesize(stretch_len=2, stretch_wid=1)
            tim.penup()
            tim.color(random.choice(COLORS))
            tim.goto(300,random.randint(-250,250))
            self.cars.append(tim)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


