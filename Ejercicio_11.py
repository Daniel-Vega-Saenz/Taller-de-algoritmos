#Entradas
Nombre=str(input("Ingrese su nombre: "))
Horas_Trab=int(input("ingrese la cantidad de horas que trabajo: "))
Pago_Norm=float(input("Digite el valor del pago por hora: "))
Hora_Ext=int(input("Ingrese las horas extras que trabajo: "))
Hijos=int(input("Ingrese la cantidad de Hijos: "))
#Caja negra
Sueldo_b=Horas_Trab*Pago_Norm
Pago_ext=Pago_Norm+((Hora_Ext*Pago_Norm)*0.25)
Actual_aca=250000
Prima=180000
Sueldo_total=Actual_aca+Prima+(173000*Hijos)+Pago_ext
Deduc=Sueldo_b-(Sueldo_b*0.14)
Sueldo_Neto=Deduc+Sueldo_total
#Salidas
print(Nombre)
print("Su sueldo neto es de: ", Sueldo_Neto)
print("Su pago por horas extra es: ", Pago_ext)
print("Sus deducciones son de: ", Deduc)