'''
Created on May 4, 2019

@author: s271486
'''
from enum import Enum

class Information():
    def __init__(self, person, address):
        self.person = person
        self.address = address
    def nineone(self):
        self.nineone_str = str.sef.address
        return self.nineone_str

user = input("Enter your name:")
useraddress = input("Enter your address:")


user_address = Information(user, useraddress)
print (user_address.person + ' ' + user_address.address )