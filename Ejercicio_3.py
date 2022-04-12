#Entradas
Venta1=float(input("Digite el valor de la compra 1: "))
Venta2=float(input("Digite el valor de la compra 2: "))
Venta3=float(input("Digite el valor de la compra 3: "))
Sueldo=float(input("Digite su salario base: "))
#Caja negra
Comision=(Venta1+Venta2+Venta3)*0.10
Total=Sueldo+Comision
#Salida
print("Su comision seria de: ", Comision)
print("Su salario total sera de : ", Total)