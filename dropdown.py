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
    myLabel = Label(root, text=selection.get()).pack()



# Options can be in a list
options = ["Monday", 
            "Tuesday", 
            "Wednesday", 
            "Thursday", 
            "Friday"
        ]

# Need a tkinter variable for our dropdown menu
selection = StringVar()
selection.set(options[0])

# Dropdown menu is called OptionMenu. 
# drop = OptionMenu(root, selection, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# have to put an asterisk in front of the list name or it ends up all on the same line.

drop = OptionMenu(root, selection, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()
# And the main event loop
root.mainloop()

