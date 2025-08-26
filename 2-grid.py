# import tk
from tkinter import *

# create root window
root=Tk()

# title
root.title("Demonstrate Grid")

# geometry
# root.geometry("400x400")

# Create two label widgets
myLabel1 = Label(root, text="Line 1")
myLabel2 = Label(root, text="Line 2")

# Arrange according to a grid, specifying the row and the column
# rows and columns are relative to each other. Changing myLabel2 column to 5 does
# nothing in this case.
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
