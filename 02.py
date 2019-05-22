'''
Created on Apr 17, 2019

@author: s271486
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
    Sunday =0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    
    
def Check():
    day= int(TextBox.get())
    if day <= 0 or day > 7:
        Result = Label(root, text = "ERROR! Please type a num between 0 and 6")
        Result.pack()
        
    else:
        for num in range(len(WeekDays)):
            Result = Label(root, text = WeekDays(num).name + " " + str(WeekDays(num).value))
            Result.pack()
            
        Result = Label(root, text = "Your favourite day is:" + " " + WeekDays(day).name + " " + str(WeekDays(day).value))
        Result.pack()

Button1 = Button(root, text= "Check", command=Check)
Button1.pack()

root.mainloop()