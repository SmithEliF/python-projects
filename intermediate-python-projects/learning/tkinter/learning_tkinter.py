from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

my_label = Label(text = "I am a label", font=("Courier", 20, "bold"))
my_label.pack(side = "left")

my_label.config(text="Hi")

my_button = Button(text="Button")
my_button.pack(side="right")

my_textbox = Text()
my_textbox.insert(END, "Hello")
my_textbox.pack()

window.mainloop()