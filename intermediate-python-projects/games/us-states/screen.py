from turtle import Screen as s, Turtle

class Screen:

    def __init__(self):

        self.map = "intermediate-python-projects/games/us-states/blank_states_img.gif"
        self.s = s()
        self.s.title("U.S States Game")
        self.s.bgpic(self.map)
        self.s.setup(750, 600)

    def user_input(self):

        return self.s.textinput(title = "Guess the State", prompt = "What's another state's name?: ")