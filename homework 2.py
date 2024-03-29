#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:06:23 2019

@author: heroname
"""
# define variables
student_list = list() # list for student objects
count = 0 # loop counter

class Student:
    def get_cwid(self):
        return self._cwid
    def set_cwid(self, cwid):
        self._cwid = cwid
    cwid = property(get_cwid, set_cwid)

    def get_first_name(self):
        return self._first_name
    def set_first_name(self, first_name):
        self._first_name = first_name
    first_name = property(get_first_name, set_first_name)
    
    def get_last_name(self):
        return self._last_name
    def set_last_name(self, last_name):
        self._last_name = last_name
    last_name = property(get_last_name, set_last_name)
    
    def get_gender(self):
        return self._gender
    def set_gender(self, gender):
        self._gender = gender
    gender = property(get_gender, set_gender)

    def get_birth_date(self):
        return self._birth_date
    def set_birth_date(self, birth_date):
        self._birth_date = birth_date
    birth_date = property(get_birth_date, set_birth_date)
    
    def get_class_id(self):
        return self._class_id
    def set_class_id(self, class_id):
        self._class_id = class_id
    class_id = property(get_class_id, set_class_id)
    
    def get_class_date(self):
        return self._class_date
    def set_class_date(self, class_date):
        self._class_date = class_date
    class_date = property(get_class_date, set_class_date)

    def get_grade(self):
        return self._grade
    def set_grade(self, grade):
        self._grade = grade
    grade = property(get_grade, set_grade)
# ---------- end class (Student)  ----------

# ---------- functions ----------
def input_string(data): # create student objects with split data and add student objects to a list
    # define variables
    student = Student()
    
    # split data into sections
    data_list = data.split(', ')
        
    for e in data_list:
        # separate key and value from data sections
        key, value = e.split(':')
        
        # assign values to student object
        if key == "CWID":
            student.cwid = value
        if key == "FirstName":
            student.first_name = value
        if key == "LastName":
            student.last_name = value
        if key == "Gender":
            student.gender = value
        if key == "Birthdate":
            student.birth_date = value
        if key == "ClassID":
            student.class_id = value
        if key == "ClassDate":
            student.class_date = value
        if key == "Grade":
            student.grade = value
            
    # add current student to the list of all students
    student_list.append(student)
# ----- end input_string(data) -----

def output(index): # format string
    return '{:^12s}{:15s}{:10s}{:^9s}{:>5s}'.format(student_list[index].cwid, student_list[index].first_name, student_list[index].last_name, student_list[index].class_id, student_list[index].grade)
# ----- end output(index) -----

def write_file(filename): # write to file
    count = 0 # reset count
    
    f = open(filename, mode='w') # write output file, reset file if necessary
    f = open(filename, mode='a') # append to output file
    
    # add table heading
    f.writelines('{:^12s}{:15s}{:10s}{:^9s}{:>5s}'.format("CWID", "First Name", "Last Name", "Class ID", "Grade"))
    f.writelines("\n")
    
    # add data to table
    while count < len(student_list):
        f.writelines(output(count))
        
        # create new line
        if count != len(student_list)-1:
            f.writelines("\n")
        
        # update loop count
        count += 1
    # ---------- end while loop (count < len(student_list)) ----------
    f.close()
# ----- end write_file() -----
# ---------- end functions ----------

# title and info
border = '====={0:^50}====='
title = border.format('Student Academic Records')
print(title)
print("This program creates a file that contains a table for inputted student academic records.")
print("Please enter the data of the students using 'CWID:__, FirstName:__, LastName:__, Gender:__, BirthDate:__, ClassID:__, ClassDate:__, Grade:__'\n")

file = input("Please enter the name of the file: ")
students = int(input("Please enter the number of students : "))
    
# student data input
while count < students:
    # track current student count
    print("Student ", count + 1, "/", students)
    data_string = input("Enter data : ")
    input_string(data_string)
    
    # update loop count
    count += 1
# ---------- end while loop (count < students) ----------

write_file(file)