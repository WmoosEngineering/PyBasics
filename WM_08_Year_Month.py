# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:24:28 2019

@author: Wmoos
"""

def isyear(year):
    if year%4==0 and year%100!=0 or year%400==0:  
        return True
    else:
        return False
    
def mesan(a,m):
    if m>=1 and m<=12:
        mes=[31,0,31,30,31,30,3,31,30,31,30,31] 
        if isyear(a)==True:
           mes[1]=29
        else:
           mes[1]=28       
    
        print(a,mes[m-1])
    else:
        print("Error in month, it must be between 1-12")

testYears = [1900, 2000, 2016, 1987]
testMonths = [14, 2, 1, 11]

for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = mesan(yr, mo)
    
    
    