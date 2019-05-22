'''
Created on Feb 21, 2019
Created for: ICS3U
@author: Francesca Berkoh

This program is the day of the week program
'''

#open window
from tkinter import *

from enum import Enum

root = Tk()

Label1 = Label(root, text="Enter the number of your favourite day of the week:")
Label1.pack()

TextBox = Entry(root)
TextBox.pack()


class WeekDays(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday =7

def Check():
    day= int(TextBox.get())
    if day <= 0 or day > 7:
        Result = Label(root, text = "ERROR! Please type a num between 0 and 6")
        Result.pack()
        
    else:
        Result = Label(root, text = "Your favourite day is:" + " " + WeekDays(day).name)
        Result.pack()

Button1 = Button(root, text= "Check", command=Check)
Button1.pack()


root.mainloop()