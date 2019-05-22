'''
Created on Apr 23, 2019

@author: s271486
'''

from enum import Enum

class street (Enum):
    AV = "Avenue"
    BLVD = "Boulavard"
    CRES = "Crescent"
    DR= "Drive"
    VISTA ="Vista"
    
class Province(Enum):
    AB = "Alberta"
    BC = "British Columbia"
    MB = "Manitoba"
    NB = "New_Brunswick"
    NL ="Newfoundland_Labrador"
    NT = "Northwest_Territories"
    NS = "Nova Scotia"
    NU = "Nunavut"
    ON = "Ontario"
    PE = "Prince_Edward"
    QC = "Quebec"
    SK= "Saskatchewn"
    YT = "Yukon"
    
class Information():
    def __init__(self, person, address, postal_code, street, province):
        self.person = person
        self.address = address
        self.postal_code = postal_code
        self.street = street
        self.province = province

user = input("Enter your name:")
useraddress = input("Enter your address:")
userpostal_code = input("Enter municipality, province and postal code:")
userstreet = input("Enter your street type:")
user_province = input("Enter your province:")




user_address = Information(user, useraddress, userpostal_code, street(userstreet).name, Province(user_province).name)
print (user_address.person + ' ' + user_address.address + " " + user_address.postal_code + " " + user_address.street + " " + user_address.province)