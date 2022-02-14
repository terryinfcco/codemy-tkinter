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
    # added after database was created
    database = "codemy", 
)

# This should tell us the connector worked.
# print(mydb)

# Create a cursor for the database and initialize it.
my_cursor = mydb.cursor()

# Create database - only run once
# my_cursor.execute("CREATE DATABASE codemy")

# Test to see if database was created
# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#     print(db)

# Create a table - again only run once
my_cursor.execute("CREATE TABLE IF NOT EXISTS customers (first_name VARCHAR(255), \
       last_name VARCHAR(255), \
       zipcode INT(10), \
       price_paid DECIMAL(10, 2), \
       user_id INT AUTO_INCREMENT PRIMARY KEY)")

# Alter the table to add more fields:
'''
my_cursor.execute("ALTER TABLE customers ADD ( \
    email VARCHAR(255), \
    address_1 VARCHAR(255), \
    address_2 VARCHAR(255), \
    city VARCHAR(50), \
    state VARCHar(50), \
    country VARCHAR(255), \
    phone VARCHAR(255), \
    payment_method VARCHAR(50), \
    discount_code VARCHAR(255))")
'''

# show table again for testing / making sure things worked
# my_cursor.execute("SELECT * FROM customers")
# print (my_cursor.description)
# for thing in my_cursor.description:
#    print(thing)



# And the main event loop
root.mainloop()

