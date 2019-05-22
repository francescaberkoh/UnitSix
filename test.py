'''
Created on Apr 3, 2019
@author: s271486
'''

from tkinter import *

root = Tk()

root.title("Volume of a cylinder")
root.geometry("200x400")


enterstring=Label(root, text= "Enter a word:")
enterstring.pack()

stringbox1 = Entry(root)
stringbox1.pack()

    
    
enterstring1=Label(root, text= "Enter another word")
enterstring1.pack()

stringbox2 = Entry(root)
stringbox2.pack()

def calculation():
    string1 = stringbox1.get()
    String1= string1.upper()
    
    string2 = stringbox2.get()
    String2 = string2.upper()
    
    if String1 == String2:
        Yes = Label(root, text = "They are the same")
        Yes.pack()
    else:
        No = Label(root, text= "They are not the same")
        No.pack()

Check = Button(root, text="Check", command=calculation)
Check.pack()
        
        
root.mainloop() 