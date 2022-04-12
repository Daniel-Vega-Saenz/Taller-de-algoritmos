#Entradas
mujeres=int(input("Escriba la cantidad de mujeres: "))
Hombres=int(input("Escriba la cantidad de hombres: "))
#Caja negra
Total_estudiantes=mujeres+Hombres
Por_M=round((mujeres*100)/Total_estudiantes,2)
Por_H=round((Hombres*100)/Total_estudiantes,2)
#Salidas
print("El porcentaje de Mujeres es: ", Por_M)
print("El porcentaje de Hombres es: ", Por_H)
print("El total de estudiantes es: ", Total_estudiantes)