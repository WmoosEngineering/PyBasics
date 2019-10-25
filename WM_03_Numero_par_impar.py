# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:32:48 2019

@author: Wmoos
"""

numero=int(input("Ingrese un numero "))
num=numero%2

if numero==0:
    str4="cero "
elif num==1:
    str4="impar"     
else:
    str4="Numero par "
print(str4)

