# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:25:24 2019

@author: Wmoos
"""
#
#def message():
#    print("Enter a value: ")
#    
#message()
#a=int(input())
#message()
#b=int(input())
#message()
#c=int(input())


#def hi(name):
#    print("Hi, ",name)
#hi("Victor")
#

#
#def hiAll(name1,name2):
#    print("Hi",name1)
#    print("Hi",name2)
#    
#hiAll(2+9,"HUGO")

#
#def address(street,city,postalcode):
#    print("Your address is: ", street,"St.,", city,postalcode)
#s  = input("Street: ")
#pC = input("Postal Code:: ")
#c  = input("City: ")
#address(s,c,pC)


#def subtra(a,b):
#    print(a-b)
#subtra(5,2)
#subtra(0,5)
#subtra(-2,-6)



#subtra(a=5,2) #error
    

#def mul(a,b):
#    return a*b
#
#print(mul(3,5))
#
#print(mul(5,9))    



#def wishes2():
#    return "HBD"
#
#w=wishes2()
#
#print(w)
#
#
#def wishes():
#    print("MW")
#    return "HBD"
#
#wishes()
#
#print(wishes())
#
#
#
#
#def hiev(myList):
#   for name in myList:
#       print("Hi, ", name)
#hiev(["Adam","Adam2","Adam3"])
#
#def createList(n):
#    myList=[]
#    for i in range(n):
#        myList.append(i)
#    return myList
#
#print(createList(5))
    

"""
http://progra.usm.cl/apunte/materia/index.html

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


       




