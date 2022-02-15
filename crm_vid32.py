from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import csv

# Create a tkinter instance root is customary but can name it anything.
root = Tk()

# Put a caption or title on our window
root.title("Customer Records Management")
root.iconphoto(False, PhotoImage(file='TD.png'))

# Set the size of the window
root.geometry("400x600")

# To get going, while in the venv.
# sudo apt install mysql-server
# gave it password password1234.
# Using pip install mysql-connector gave an error so uninstalled it.
# Then had to pip install mysql-connector-python.

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password1234",
    # added after database was created
    database="codemy",
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

# Clear Text Fields


def clear_fields():
    first_name_box.delete(0, END)
    last_name_box.delete(0, END)
    address1_box.delete(0, END)
    address2_box.delete(0, END)
    city_box.delete(0, END)
    state_box.delete(0, END)
    zipcode_box.delete(0, END)
    country_box.delete(0, END)
    phone_box.delete(0, END)
    email_box.delete(0, END)
    payment_method_box.delete(0, END)
    discount_code_box.delete(0, END)
    price_paid_box.delete(0, END)

# Submit Customer to Database


def add_customer():
    sql_command = "INSERT INTO customers (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (first_name_box.get(), last_name_box.get(), zipcode_box.get(), price_paid_box.get(), email_box.get(), address1_box.get(
    ), address2_box.get(), city_box.get(), state_box.get(), country_box.get(), phone_box.get(), payment_method_box.get(), discount_code_box.get())
    my_cursor.execute(sql_command, values)

    # Commit the changes to the database
    mydb.commit()
    # when done adding, clear fields
    clear_fields()

# Write to CSV file
def write_to_csv(result):
    # Going to append to the file.
    with open('customers.csv', 'a', newline='') as f:
        w = csv.writer(f, dialect='excel')
        for record in result:
            w.writerow(record)

def list_customers():
    # First create a new window.
    list_customer_query = Tk()
    list_customer_query.title("List All Customers")
    # list_customer_query.iconphoto(False, PhotoImage(file='TD.png'))
    list_customer_query.geometry("800x600")
    # Query database
    # Show the data in the database
    my_cursor.execute("SELECT * FROM customers")
    # result will contain the whole database
    result = my_cursor.fetchall()
    # enumerated for loop creates an index number as well as x which is each row of the database
    for index, x in enumerate(result):
        # num counts the columns
        num = 0
        # so x is each row of the table, so y will be each column in the row.
        for y in x:
            lookup_label = Label(list_customer_query, text=y)
            lookup_label.grid(row=index, column=num, sticky=W)
            num += 1
    # button to export to csv file.
    csv_button = Button(list_customer_query, text="Save to CSV",
                        command=lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)


# Now create the gui for our application, first the labels
title_label = Label(root, text="Customer Database", font=("Helvetica, 16"))
title_label.grid(row=0, column=0, columnspan=2, pady="10")

first_name_label = Label(root, text="First Name").grid(
    row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text="Last Name").grid(
    row=2, column=0, sticky=W, padx=10)
address1_label = Label(root, text="Address 1").grid(
    row=3, column=0, sticky=W, padx=10)
address2_label = Label(root, text="Address 2").grid(
    row=4, column=0, sticky=W, padx=10)
city_label = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text="State").grid(
    row=6, column=0, sticky=W, padx=10)
zipcode_label = Label(root, text="Zipcode").grid(
    row=7, column=0, sticky=W, padx=10)
country_label = Label(root, text="Country").grid(
    row=8, column=0, sticky=W, padx=10)
phone_label = Label(root, text="Phone Number").grid(
    row=9, column=0, sticky=W, padx=10)
email_label = Label(root, text="Email Address").grid(
    row=10, column=0, sticky=W, padx=10)
payment_method_label = Label(root, text="Payment Method").grid(
    row=11, column=0, sticky=W, padx=10)
discount_code_label = Label(root, text="Discount Code").grid(
    row=12, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text="Price Paid").grid(
    row=13, column=0, sticky=W, padx=10)

# Now the entry boxes
first_name_box = Entry(root)
first_name_box.grid(row=1, column=1)
last_name_box = Entry(root)
last_name_box.grid(row=2, column=1, pady=5)
address1_box = Entry(root)
address1_box.grid(row=3, column=1, pady=5)
address2_box = Entry(root)
address2_box.grid(row=4, column=1, pady=5)
city_box = Entry(root)
city_box.grid(row=5, column=1, pady=5)
state_box = Entry(root)
state_box.grid(row=6, column=1, pady=5)
zipcode_box = Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)
country_box = Entry(root)
country_box.grid(row=8, column=1, pady=5)
phone_box = Entry(root)
phone_box.grid(row=9, column=1, pady=5)
email_box = Entry(root)
email_box.grid(row=10, column=1, pady=5)
payment_method_box = Entry(root)
payment_method_box.grid(row=11, column=1, pady=5)
discount_code_box = Entry(root)
discount_code_box.grid(row=12, column=1, pady=5)
price_paid_box = Entry(root)
price_paid_box.grid(row=13, column=1, pady=5)

# Buttons
add_customer_button = Button(
    root, text="Add Customer To Database", command=add_customer)
add_customer_button.grid(row=14, column=0, padx=10, pady=10)
clear_fields_button = Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=14, column=1)
list_customers_button = Button(
    root, text="List Customers", command=list_customers)
list_customers_button.grid(row=15, column=0, sticky=W, padx=10)


# And the main event loop
root.mainloop()
