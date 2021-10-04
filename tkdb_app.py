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

# Create a delete record function
def delete():
    # have to connect to db and create cursor inside function
    conn = sqlite3.connect('address_book.db')
    # Create a cursor - used to talk to the db
    c = conn.cursor()    

    # have to do this concanenation - not sure why but that's how it works.
    c.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())
    delete_box.delete(0, END)
    
    # after making a change to the database commit it.
    conn.commit()
    # Then close the connection
    conn.close()


# Create Submit Function for Database
def submit():
    # have to connect to db and create cursor inside function
    conn = sqlite3.connect('address_book.db')
    # Create a cursor - used to talk to the db
    c = conn.cursor()

    # Insert into table 
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        })

    # after making a change to the database commit it.
    conn.commit()
    # Then close the connection
    conn.close()

    # Clear the text boxes after grabbing the current info
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create query function
def query():
    # have to connect to db and create cursor inside function
    conn = sqlite3.connect('address_book.db')
    # Create a cursor - used to talk to the db
    c = conn.cursor()

    # Select all plus primary key which here is oid rather than rowid
    # Reading the docs makes me thing either would work.
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall() # returns a list of tuples.
    # print (records)

    print_records = ''
    for record in records:
        # print_records += str(record[0]) + " " + str(record[1]) + "\n"
        print_records += f"{record[0]} {record[1]} \t {str(record[6])} \n "

    query_label = Label(root, text=print_records) 
    query_label.grid(row=11, column=0, columnspan=2)
    # after making a change to the database commit it.
    conn.commit()
    # Then close the connection
    conn.close()


# Create the entry boxes to put the information in
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Create labels to go next to the entry boxes
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="ZipCode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="ID To Delete")
delete_box_label.grid(row=9, column=0, pady=5)
# Create Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=104)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# after making a change to the database commit it.
conn.commit()

# Then close the connection
conn.close()



# And the main event loop
root.mainloop()

