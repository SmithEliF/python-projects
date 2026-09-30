from conversion import Conversion
from tkinter import *

conversion = Conversion()

window = Tk()
window.title("Miles to Km Converter")
window.minsize(400,400)

i = Entry(width=10)
i.insert(END, string="0")
i.grid(column=1, row=0)

l1 = Label(text="Miles")
l1.grid(column=2, row=0)

l2 = Label(text="is equal to")
l2.grid(column=0, row=1)

l3 = Label(text="0")
l3.grid(column=1, row=1)

l4 = Label(text="Km")
l4.grid(column=2, row=1)

b = Button(
	text="Calculate",
	command=lambda: l3.config(text=conversion.calculate(int(i.get()))),
)
b.grid(column=1, row=2)

window.mainloop()