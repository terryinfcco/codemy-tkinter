# import tk
import tkinter as tk

# create root window
root=tk.Tk()

# title
root.title("Demonstrate Grid")

# geometry
root.geometry("400x400")

# Create two label widgets
myLabel1 = tk.Label(root, text="Line 1")
myLabel2 = tk.Label(root, text="Line 2")
 
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

root.mainloop()
