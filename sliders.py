# Video 16 Codemy.com Tkinter YouTube

from tkinter import *
from PIL import ImageTk,Image

# Create a tkinter instance root is customary but can name it anything.
root = Tk()
    
# Put a caption or title on our window
root.title("Message Boxes")
root.iconphoto(False, PhotoImage(file='TD.png'))
    
# Set the size of the window
root.geometry("400x400")

def read_sliders():
    label_v = Label(root, text=f"Vertical: {v.get()}").pack()
    label_h = Label(root, text=f"Horizontal: {h.get()}").pack()

def resize_window(var):
    # not sure why you have to define a parameter but you do.
    root.geometry(f"{h.get()}x{v.get()}")

# sliders - it's called the scale widget
# vertical orientation is the default
v = Scale(root, from_=0, to=400, label="Height", command=resize_window)
v.set(400)
# don't pack scale with a .pack - use its own line.
v.pack()

h = Scale(root, from_=0, to=400, orient=HORIZONTAL, label="Width", command=resize_window)
h.set(400)
h.pack()

# btn = Button(root, text="Show Slider Values", command=read_sliders).pack()
# or could change window size based on sliders
# btn2 = Button(root, text="Change Window Size", command=resize_window).pack()

# And the main event loop
root.mainloop()

