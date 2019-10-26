# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:46:06 2019

@author: Wmoos
"""

def isyear(year):
    if year%4==0 and year%100!=0 or year%400==0:  
        return True
    else:
        return False
    
def mesan(a,m,d):
   if  d>=1 and d<=31: 
        if m>=1 and m<=12:
            mes=[31,0,31,30,31,30,3,31,30,31,30,31] 
            if isyear(a)==True:
               mes[1]=29
               print("366 dias")
            else:
               mes[1]=28    
               print("365 dias")
        
            #print(a,mes[m-1])
        else:
            print("Error in month, it must be between 1-12")
   else:
            print("Error in day, it must be between 1-31")
        

testYears  = [1900, 2000, 2016, 1987]
testMonths = [14, 2, 1, 11]
testDays   = [14, 2, 1, 40]

for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    dy = testDays[i]
    print(yr, mo, dy,"->", end="")
    result = mesan(yr, mo,dy)
    
    

