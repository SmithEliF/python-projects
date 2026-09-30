from turtle import Screen as s

class Screen:

    def __init__(self):

        self.screen = s()
        self.screen.setup(600, 600)
        self.screen.tracer(0)