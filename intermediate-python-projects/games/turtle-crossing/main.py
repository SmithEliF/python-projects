from screen import Screen
from player import Player
from car import Car
from turtle import TK
from scoreboard import Scoreboard

car = Car()
screen = Screen()
player = Player()
scoreboard = Scoreboard()

screen.screen.listen()
screen.screen.onkey(player.move, "space")

def game_tick():
    scoreboard.update_scoreboard()
    screen.screen.update()
    car.create_car()
    car.move()
    for traffic_car in car.all_cars:
        if traffic_car.distance(player) < 20:
            TK.messagebox.showinfo(message = "Game Over")
            screen.screen.bye()
    if player.is_at_finish():
        player.goto(0,-280)
        car.level_up() 
        scoreboard.point()
    screen.screen.ontimer(game_tick, 100)

game_tick()
screen.screen.mainloop()