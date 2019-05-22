'''
Created on Apr 17, 2019

@author: s271486
'''

class Information():
    def __init__(self, person, address, postal_code):
        self.person = person
        self.address = address
        self.postal_code = postal_code

user = input("Enter your name:")
useraddress = input("Enter your address:")
userpostal_code = input("Enter municipality, province and postal code:")

user_address = Information(user, useraddress, userpostal_code)
print (user_address.person + ' ' + user_address.address + " " + user_address.postal_code)