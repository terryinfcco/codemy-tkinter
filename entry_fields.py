# Import all of tkinter
from tkinter import *

# Create root window - Main window of your applicaton usually called root, but
# doesn't have to be. Has to be first in program.
root = Tk()

# Create an entry widiget and call it e
# width is the size of the input box in characters. Can change the borderwidth on
# all of these widgets. bg and fg work here also.
e = Entry(root, width=50, borderwidth=5)

# Can put default text in the box (it's box 0, I assume we'll get to that later)
# You have to clear the text before typing.
e.insert(0, "Enter Your Name:")
e.pack()

# Create a button. Need a function that the button calls first.

def myClick():
# e.get gets whatever character the entry box contains
#     myLabel = Label(root, text="Hello " + e.get())
# Or you can put the contents of the entry box in a variable
    name = e.get()
    myLabel = Label(root, text="Hello " + name)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()


# Create event loop
root.mainloop()
