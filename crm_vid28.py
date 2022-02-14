from tkinter import *
from PIL import ImageTk,Image
import mysql.connector

# Create a tkinter instance root is customary but can name it anything.
root = Tk()
    
# Put a caption or title on our window
root.title("Customer Records Management")
root.iconphoto(False, PhotoImage(file='TD.png'))
    
# Set the size of the window
root.geometry("400x400")

# To get going, while in the venv.
# sudo apt install mysql-server
# gave it password password1234. 
# Using pip install mysql-connector gave an error so uninstalled it.
# Then had to pip install mysql-connector-python.

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password1234",
)

# This should tell us the connector worked.
print(mydb)

# And the main event loop
root.mainloop()

