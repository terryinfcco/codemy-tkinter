from tkinter import *
from PIL import ImageTk,Image

# Create a tkinter instance root is customary but can name it anything.
root = Tk()
    
# Put a caption or title on our window
root.title("Message Boxes")
root.iconphoto(False, PhotoImage(file='TD.png'))
    
# Set the size of the window
root.geometry("400x400")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack(pady=10)
    # To delete what was entered in the text box
    e.delete(0, 'end')

# Demo how to change the height of an entry box
# Only way to change the height is to make the textsize bigger
e = Entry(root, width=50, font=('Helvetica', 24))
e.pack(padx=10, pady=10)

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack(pady=10)


# And the main event loop
root.mainloop()

