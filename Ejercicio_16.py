#Entradas
Gal=float(input("Ingrese la cantidad de galones que recargo: "))
#caja negra
Conver=(Gal*3785)/1
Total=round(Conver*50000, 5)
#Salida
print("El cliente debe de pagar: ", Total)
