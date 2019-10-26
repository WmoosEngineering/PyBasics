# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:48:04 2019

@author: Wmoos
"""

def isyear(year):
    if year%4==0 and year%100!=0 or year%400==0:  
        return True
        
    

testData = [1900, 2000, 2016, 1987,2001,2002,2004]
testResults = [False, True, True, False, False,False,True]


for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isyear(yr)
	if result == testResults[i]:
		print("Bisiesto")
	else:
		print("No bisiesto")





