# Codemy.com Youtube Tkinter Video 19
# Using sqlite3 database which comes with python

from tkinter import *
from PIL import ImageTk,Image
import sqlite3

# Create a tkinter instance root is customary but can name it anything.
root = Tk()
    
# Put a caption or title on our window
root.title("Message Boxes")
root.iconphoto(False, PhotoImage(file='TD.png'))
    
# Set the size of the window
root.geometry("400x400")

#  Create a database or connect to an existing database - command same either way
conn = sqlite3.connect('address_book.db')

# Create a cursor - used to talk to the db
c = conn.cursor()

# tables inside database do the actual work, like a spreadsheet
# This only needs to be run once to create the db and table
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")

# after making a change to the database commit it.
conn.commit()

# Then close the connection
conn.close()



# And the main event loop
root.mainloop()

