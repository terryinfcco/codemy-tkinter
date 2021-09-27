# import tkinter module as tk
import tkinter as tk
from PIL import ImageTk,Image
  
# Create a tkinter instance root is customary but can name it anything.
root = tk.Tk()
    
# Put a caption or title on our window
root.title("Hello World!")
    
# Set the size of the window
# root.geometry("400x400")

root.iconphoto(False, tk.PhotoImage(file='TD.png'))

# Create a frame and give it some padding inside the frame. In this case around the button.
frame = tk.LabelFrame(root, text="This is my Frame", padx=15, pady=15)
# Pack it and add some padding outside the frame. 
frame.pack(padx=100, pady=100)

b = tk.Button(frame, text="Don't Click Here!")
b2 = tk.Button(frame, text="...or here!")

# Note you can do grid inside a packed frame.
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

# And the main event loop
root.mainloop()

