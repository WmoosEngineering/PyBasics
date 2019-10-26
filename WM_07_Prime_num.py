# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:56:15 2019

@author: Wmoos
"""

def isPrime(n):
    a=0
    for i in range(1,n+2):
        if n%i==0:
            a=a+1
    return a


for j in range(1,20):
    r=isPrime(j)

    if r==2:
         print(j)
