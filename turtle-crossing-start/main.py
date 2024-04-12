import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
carmanager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.movee,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.car_move()
    #DETECT COLLISION WITH CAR
    for car in carmanager.all_car:
       if car.distance(player) < 20:
          game_is_on =False
          score.game_over()

    #DETECT IT REACHES OTHER SIDE
    if player.is_finish():
       player.goto_start()
       carmanager.level_up()
       score.inc_lv()


screen.exitonclick()