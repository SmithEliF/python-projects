from screen import Screen
from game_timer import Timer
import turtle
import pandas
from turtle import TK

screen = Screen()
timer = Timer()
data = pandas.read_csv("intermediate-python-projects/games/us-states/50_states.csv")
states = data["state"].to_list()
guessed_states = []
screen_guessed_states = turtle.Turtle()
screen_guessed_states.pu()
screen_guessed_states.hideturtle()
screen_guessed_states.goto(-350, 250)

def write_to_screen(x, y, state):
    output = turtle.Turtle()
    output.hideturtle()
    output.pu()
    output.goto(x, y)
    output.write(state)

def game_tick():
    if timer.timer > 0:
        timer.countdown()
        timer.update_timer()
        screen.s.ontimer(game_tick, 1000)

def user_input():
    if timer.timer > 0:
        answer = screen.user_input().capitalize()
        if answer in states:
            if answer not in guessed_states:
                state_data = data[data.state == answer]
                x = state_data.x.item()
                y = state_data.y.item()
                write_to_screen(x, y, answer)
                guessed_states.append(answer)
                update_guessed()
        elif answer == "Exit" or timer.timer == 0:
            missed_states = [state for state in states if state not in guessed_states]
            df = pandas.DataFrame(missed_states)
            df.to_csv("intermediate-python-projects/games/us-states/states_to_learn.csv")
            screen.s.bye()
        screen.s.ontimer(user_input, 0)

def update_guessed():
    screen_guessed_states.clear()
    screen_guessed_states.write(f'{len(guessed_states)}/50', font=("Courier", 30, "normal"))

update_guessed()
screen.s.ontimer(game_tick, 1000)
screen.s.ontimer(user_input, 0)

turtle.mainloop()