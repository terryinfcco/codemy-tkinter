
# First import tkinter
from tkinter import *

# Had to install Pillow with pip3 in the venv
# Now import the pieces we need
# There is a built in image library with python but it's very limited.

from PIL import ImageTk, Image
# Now create the main window. Typically called root,
# but can be named most anything.
root = Tk()
root.title('Learn to Code at Codemy.com')

# This is the way to do what html/css would call a favicon
# The way he shows on the video doesn't work in Linux,
# although I assume it's just fine in Windows.

# This is how he showed to do it on Windows
# For some reason I can't get it to find the file on Linux
# root.iconbitmap('/home/terry/github/codemy-tkinter/calculator.png')

# This works on linux
root.iconphoto(False, PhotoImage(file='calculator.png'))

# Now let's show an image
# Define where the image is
my_img = ImageTk.PhotoImage(Image.open("images/82479_02.jpg"))
# Images can be added to most (all?) tkinter widgets -
# here we'll put it on a label
my_label = Label(root, image=my_img)
my_label.pack()

# Doing an exit button really simple

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

# Create the event loop that waits for user to do things on the screen

root.mainloop()

