# import tkinter module as tk
from tkinter import *
from PIL import ImageTk,Image
# Need to import messagebox to use them
from tkinter import messagebox

# Create a tkinter instance root is customary but can name it anything.
root = Tk()
    
# Put a caption or title on our window
root.title("Message Boxes")
root.iconphoto(False, PhotoImage(file='TD.png'))
    
# Set the size of the window
root.geometry("400x400")

def popup():
    # Returns ok for OK (only choice)    
    # messagebox.showinfo("Titlebar", "Message To Show")
    # Returns ok for OK (only choice)    
    # messagebox.showwarning("Titlebar", "Message To Show")
    # Returns ok for OK (only choice)    
    # messagebox.showerror("Titlebar", "Message To Show")
    # Returns "yes" for yes and "no" for no
    # messagebox.askquestion("Titlebar", "Message To Show")
    # returns 1 for OK, 0 for Cancel
    # messagebox.askokcancel("Titlebar", "Message To Show")

    # returns 1 for Yes and 0 for No
    response = messagebox.askyesno("Titlebar", "Message To Show")
    
    if response == 1:
        Label(root, text="You Clicked Yes").pack()
    else:
        Label(root, text="You Clicked No").pack()

Button(root, text="Popup", command=popup).pack()
    
# And the main event loop
root.mainloop()

