# Import everything from tkinter
from tkinter import *

# In tkinter everything is a widget. 
# Create the root widget (main window)

root = Tk()

# Create a label widget so we can show some text.
# Creating a widget in tkinter is a two step process - create the widget and display it.

# Create the widget. Specify where the widget goes (root), and some text.
myLabel = Label(root, text="Hello World!")
# Use pack to display the widget
myLabel.pack()

# Create the event loop - in tkinter called the mainloop
root.mainloop()






