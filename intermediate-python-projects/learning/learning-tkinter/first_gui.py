from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click me")
new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=3)

window.mainloop()