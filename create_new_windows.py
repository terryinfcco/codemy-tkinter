# Video 14 Codemy Youtube

from tkinter import *
from PIL import ImageTk,Image

# Create a tkinter instance root is customary but can name it anything.
root = Tk()
    
# Put a caption or title on our window
root.title("Create New Windows")
root.iconphoto(False, PhotoImage(file='TD.png'))
    
# Set the size of the window
root.geometry("400x400")

def open2nd():
    # When using this second window the plain label that's commented out works, 
    # but the label with an image doesn't. For whatever reason python needs my_img to be a global
    global my_img
    # Create a 2nd window using Toplevel method
    top = Toplevel()
    # Can set a title and icon
    top.title("Second Window")
    top.iconphoto(False, PhotoImage(file='TD.png'))
    # top.geometry("500x500")
    # then use new window name (top here) instead of root for location
    # can do anything in this new window that you can do in the root window.
    # lbl = Label(top, text="Hello World!").pack()
    my_img = ImageTk.PhotoImage(Image.open("images/82479_02.jpg"))
    my_label = Label(top, image=my_img).pack()
    # Then to close the window - destroy it
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()



btn = Button(root, text="Open Second Window", command=open2nd).pack()
# And the main event loop
root.mainloop()

