# import tkinter module as tk
import tkinter as tk
from PIL import ImageTk,Image

# Create a tkinter instance root is customary but can name it anything.
root = tk.Tk()
    
# Put a caption or title on our window
root.title("Hello World!")
root.iconphoto(False, tk.PhotoImage(file='TD.png'))
    
# Set the size of the window
root.geometry("400x400")
    
# And the main event loop
root.mainloop()

