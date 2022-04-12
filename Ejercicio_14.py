#Entradas
Ant=float(input("Ingrese la lectura anterior: "))
Aho=float(input("Ingrese la lectura actual: "))
KV=float(input("Ingrese el valor del kilovatio: "))
#Caja negra
Promedio=(Ant+Aho)/2
Total=Promedio*KV
#Salidas
print("Usted pagararia en el mes: ", Total)