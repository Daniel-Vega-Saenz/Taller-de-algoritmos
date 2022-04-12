#Entradas
HorasT=int(input("Ingrese el numero de horas trabajadas: "))
#Caja Negra
Salario_total=(HorasT*4167)
Descuento=Salario_total*0.20
Salario_neto=Salario_total-Descuento
#Salidas
print("Por trabajar esa cantidad de horas, su salario neto es: ", Salario_neto)