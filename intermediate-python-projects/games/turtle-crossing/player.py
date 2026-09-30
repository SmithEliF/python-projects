from  turtle import Turtle

class Player(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.pu()
        self.goto(0,-280)

    def move(self):

        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def is_at_finish(self):
        return self.ycor() >= 280