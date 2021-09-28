# import tk
import tkinter as tk
from typing_extensions import IntVar
from PIL import ImageTk,Image

# create root window
root=tk.Tk()

# title
root.title("Radio Buttons")

# geometry and an icon in the corner
root.geometry("400x400")
root.iconphoto(False, tk.PhotoImage(file='TD.png'))

# Create a tkinter integer variable.
r = tk.IntVar()
r.set(2)

# A string tkinter variable would be
# s = tk.StringVar

def clicked(value):
    myLabel = tk.Label(root, text=value)
    myLabel.pack()

# Create the radio buttons, using a tkinter variable called r.
tk.Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
tk.Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel = tk.Label(root, text=r.get())
myLabel.pack()

myButton = tk.Button(root, text="Click Me!", command=lambda: clicked(r.get()))
myButton.pack()

root.mainloop()
