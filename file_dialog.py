# Codemy Video 15 Tkinter YouTube

from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

# Create a tkinter instance root is customary but can name it anything.
root = Tk()
    
# Put a caption or title on our window
root.title("Message Boxes")
root.iconphoto(False, PhotoImage(file='TD.png'))
    
# Set the size of the window
# root.geometry("400x400")
def open():
    global my_image
    # filedialog locates a file and returns the path and filename
    # can do specific types or all files.
    root.filename = filedialog.askopenfilename(initialdir="/home/terry/sync_pictures", title="Select a File", filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))
    # root.filename = filedialog.askopenfilename(initialdir="/home/terry", title="Select a File", filetypes=(("all files", "*.*"))
    
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    image_label = Label(root, image=my_image).pack()
    filename_label = Label(root, text=root.filename).pack()
    
my_btn = Button(root, text="Open File", command=open).pack()

# And the main event loop
root.mainloop()

