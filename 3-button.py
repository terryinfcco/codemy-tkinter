# Import all of tkinter
from tkinter import *

# Create root window - Main window of your applicaton usually called root, but
# doesn't have to be. Has to be first in program.
root = Tk()

# Create a button. Need a function that the button calls first.

def myClick():
    myLabel = Label(root, text="You clicked the Button!!")
    myLabel.pack()

# Use command= to call a function. Notice that there are no parentheses
# for parameters. Passing parameters is possible with lambda, but if
# you put parentheses without lambda it won't work right.

myButton = Button(root, text="Click Me!", command=myClick)

# Change the foreground color with fg and background color with bg
# Can also use hex codes bg="#ffffff" or fg="#000000"
myButton4 = Button(root, text="Showing Colors", fg="blue", bg="orange")

# Add padding which is inside the button borders
myButton2 = Button(root, text="Showing padding", padx=50, pady=50)

# if you want the button grayed out so it can't be clicked:
myButton3 = Button(root, text="Showing Disabled", state=DISABLED)

myButton.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()

# Create event loop
root.mainloop()
