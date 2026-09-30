from turtle import Turtle
import datetime

class Timer:

    def __init__(self):
        self.timer = 600
        self.screen_timer = Turtle()
        self.screen_timer.pu()
        self.screen_timer.hideturtle()
        self.screen_timer.goto(175, 250)

    def countdown(self):
        self.timer -= 1

    def update_timer(self):
        self.screen_timer.clear()
        self.screen_timer.write(datetime.timedelta(seconds = self.timer), font=("Courier", 30, "normal"))