#Entradas
Cf1=float(input("Ingrese la nota de la calificacion 1: "))
Cf2=float(input("Ingrese la nota de la calificacion 2: "))
Cf3=float(input("Ingrese la nota de la calificacion 3: "))
Exam=float(input("Ingrese la nota del examen final: "))
Trab=float(input("Ingrese la nota del trabajo final: "))
#Caja negra
Cftotal=(((Cf1+Cf2+Cf3)/3)*0.55)
Examtotal=(0.30*Exam)
Trabtotal=(0.15*Trab)
Nota_final=(Cftotal+Examtotal+Trabtotal)
#Salidas
print("su nota final es: ", Nota_final)