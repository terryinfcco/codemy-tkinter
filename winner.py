from tkinter import *
from PIL import ImageTk,Image
from random import randint

# Create a tkinter instance root is customary but can name it anything.
root = Tk()
    
# Put a caption or title on our window
root.title("Random Winner")
root.iconphoto(False, PhotoImage(file='TD.png'))
    
# Set the size of the window
root.geometry("400x400")

def pick():
    entries = ['Dave', 'Kristy', 'Izie', 'Hugh', 'Marty', 'Amberly', 'Terry', 'Terry']
    # if we convert the entries list to a set which is without duplicates and then back to a list
    # we'll eliminate duplicates from the list.
    entries_set = set(entries)
    # convert back to list
    unique_entries = list(entries_set)
    # now need the length of the list for our random selection
    our_num = len(unique_entries) - 1
    # create a random number between 0 and the length of the list - 1
    rando = randint(0, our_num)

    # winnerLabel = Label(root, text=str(len(entries)) + " " + str(len(unique_entries)), font=('Helvetica', 18))
    winnerLabel = Label(root, text=unique_entries[rando], font=('Helvetica', 18))
    winnerLabel.pack(pady=50)

# Pick a winner from a list of people entering a contest. 

topLabel = Label(root, text="Win-O-Rama!", font=('Helvetica', 24))
topLabel.pack(pady=20) 

winButton = Button(root, text="PICK OUR WINNER!!", font=('Helvetica', 24), command=pick)
winButton.pack(pady=20)


# And the main event loop
root.mainloop()

