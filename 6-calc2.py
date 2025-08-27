# First of 3 videos creating a calculator with tkinter
from tkinter import *

root = Tk()

# to put a title on the window
root.title("Simple Calculator")


def button_click(number):
    # Grab what's already in the entry widget
    current = e.get()
    # clear the widget so we don't add too many copies of the numbers
    e.delete(0, END)
    # Concatenate with the number just clicked
    e.insert(0, str(current) + str(number))

def button_clear():
    # simple - clear the text box
    e.delete(0, END)

def button_add():
    # grab the contents of the text box and save it in a global variable, making sure
    # it's an integer because we want to add it.
    first_number = e.get()
    global f_num 
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, int(second_number) + f_num)

# An entry box to contain input and results
e = Entry(root, width=35, borderwidth=5)
# columnspan says to take up 3 columns in the grid
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create the calculator number buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Create the buttons that add, total and clear
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=92, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=80, pady=20, command=button_clear)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
root.mainloop()


