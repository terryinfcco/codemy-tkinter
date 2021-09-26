
# First import tkinter
from tkinter import *

# Had to install Pillow with pip3 in the ltk venv
# Now import the pieces we need

from PIL import ImageTk,Image
# Now create the main window. Typically called root,
# but can be named most anything.
root = Tk()

# This is the way to do what html/css would call a favicon
# The way he shows on the video doesn't work in Linux,
# although I assume it's just fine in Windows.

root.iconphoto(False, PhotoImage(file='calculator.png'))

# Now let's show an image
# Define where the image is
my_img = ImageTk.PhotoImage(Image.open("images/82479_02.jpg"))
# Images can be added to most (all?) tkinter widgets -
# here we'll put it on a label
my_label = Label(root,image=my_img)
my_label.pack()

# Doing an exit button really simple

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

# Create the event loop that waits for user to do things on the screen

root.mainloop()

