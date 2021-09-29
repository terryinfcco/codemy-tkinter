# Video 18 Codemy.com YouTube Tkinter

from tkinter import *
from PIL import ImageTk,Image

# Create a tkinter instance root is customary but can name it anything.
root = Tk()
    
# Put a caption or title on our window
root.title("Message Boxes")
root.iconphoto(False, PhotoImage(file='TD.png'))
    
# Set the size of the window
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

# Need a tkinter variable - used by checkbox - by default 1 means checked, 0 means unchecked
# using onvalue and offvalue you can change what's returned. If you use strings var will
# need to be a StringVar. 
var = IntVar()
c = Checkbutton(root, text="Check this box", variable=var)
# deselect by default
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

# And the main event loop
root.mainloop()

