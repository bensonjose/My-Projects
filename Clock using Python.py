
# Importing the required Libraries

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("clock")   #Mentioning the Title



# Creating a function time and specifying whether we need the 12 hour format or the 24 hour format.

def time():
    string = strftime('%H:%M:%S %p')         #('%H:%M:%S %p') to strftime('%I:%M:%S %p')    ----->To Make the Clock 12 hours format
    label.config(text=string)
    label.after(1000, time)


# Here, We Specify the font, background color etc...
label = Label(root, font=("ds-digital", 80), background="black", foreground = "cyan")
label.pack(anchor='center')
time()

mainloop()


# end//
