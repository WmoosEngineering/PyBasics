# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:03:22 2019

@author: CEC
"""

fname=input("First name: ")
lname=input("Last name: ")
loc=input("Where do you come from?: ")
age=input("How old are you: ")
strage=int(age)
space=" "
if strage>=18:
    print("She/He is"+space+fname+space+lname+","+space+"she/he is from"+space+loc+space+"and she/he is"+space+age+space+"years old and so is an adult")
else:
    print("She/He is"+space+fname+space+lname+","+space+"she/he is from"+space+loc+space+"and she/he is"+space+age+space+"years old and is a teenager")
    

