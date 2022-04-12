#entradas
#Matematicas
examen=float(input("Digite la nota del examen de Matematicas:"))
tarea1=float(input("Digite nota de la tarea 1:"))
tarea2=float(input("DIgite nota de la tarea 2:"))
tarea3=float(input("Digite la nota de la tarea 3:"))
#fisica
examen_f=float(input("Digite nota del examen de fisica:"))
tarea1_f=float(input("Digite nota de la tera 1:"))
tarea2_f=float(input("Digite nota de la tarea 2:"))
#Química
examen_q=float(input("Digite nota del examen de química:"))
tarea1_q=float(input("Digite nota de la tarea 1:"))
tarea2_q=float(input("DIgite nota de la tarea 2:"))
tarea3_q=float(input("Digite nota de la tarea 3:"))
#caja negra
Promedio_Mat=(0.9*examen)+(0.1*((tarea1+tarea2+tarea3)/3))
Promedio_Qui=(0.8*examen_q)+(0.2*((tarea1_q+tarea2_q+tarea3_q)/3))
Promedio_Fis=(0.85*examen_f)+(0.15*((tarea1_f+tarea2)/2))
Promedio_General=(Promedio_Fis+Promedio_Mat+Promedio_Qui)/3
#salidas
print("El promedio general es:",Promedio_General)