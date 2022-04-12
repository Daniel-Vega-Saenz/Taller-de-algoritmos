#Entradas
Metros=float(input("Escriba la distancia en metros: "))
#Caja negra
Pulgadas=round((Metros*39.27)/1, 2)
Pies=round((Pulgadas*1)/12, 2)
#Salida
print("Esa cantidad de metros en pulgadas es: ", Pulgadas)
print("Esa cantidad de metros en pies es: ", Pies)