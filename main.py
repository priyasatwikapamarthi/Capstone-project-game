import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)


player = Player()
car = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(fun = player.up,key = "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_cars()
    car.move_car()
    # Collision with cars
    for carz in car.cars:
        if carz.distance(player)<20:
            score_board.game_over()
            game_is_on= False

    # #Collision with wall
    if player.ycor()>280:
        player.original_position()
        score_board.increase()
        car.increase_speed()
        score_board.update()

screen.exitonclick()
