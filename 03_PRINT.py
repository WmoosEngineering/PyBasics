# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:03:11 2019

@author: CEC
"""

NAME1=input("¿Cuál es tu primer nombre? ")
NAME2=input("¿Cuál es tu primer apellido? ")
AGE1=input("¿Cuál es tu edad (AÑOS)? ")
LOC1=input("¿Cuál es tu ubicación (Ciudad)? ")
SPACE=" "
print("HOLA"+SPACE+NAME1+SPACE+NAME2+","+SPACE+"TU EDAD ES DE"+SPACE+AGE1+SPACE+"AÑOS Y TU UBICACIÓN ES EN"+SPACE+LOC1)
if int(AGE1)>=18:
    print("Es mayor de Edad")
else:
    print("Es menor de Edad")
    