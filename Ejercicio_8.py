from ast import Import
import math


#Entradas
A=float(input("Ingrese el valor del lado A: "))
B=float(input("Ingrese el valor del lado B: "))
C=float(input("Ingrese el valor del lado C: "))
#Caja negra
S=(A+B+C)/2
Area=round(math.sqrt(S*(S-A)*(S-B)*(S-C)),2)
#Salidas
print("El valor del area es: ", Area)