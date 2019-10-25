# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:04:06 2019

@author: Wmoos
"""

fn=input("Cual es tu nombre: ")
ln=input("Cual es tu apellido: ")
loc=input("Cual es tu ubicacion: ")
age=int(input("Cual es tu edad: "))

if age>=18:
    str4="Mayor de edad"
else:
    str4="Menor de edad"
    
space=""
print("\n")
str1="Hola Bienvenido"
str2="Tu"
str3="es:"
print(str1,fn,"!")
print(str2,"apellido",str3,ln)
print(str2,"ubicacion",str3,loc)
print(str2,"edad",str3,age)
print(str4)

