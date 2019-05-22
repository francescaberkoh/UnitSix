'''
Created on Apr 18, 2019

@author: s271486
'''
# Created by: Mr. Coxall
# Created on: Nov 2017
# Created for: ICS3U
# This program is an example of a structure

class Student():
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade

a_single_student = Student('Patrick', 'Coxall', 13)
print (a_single_student.first_name + ' ' + str(a_single_student.grade))