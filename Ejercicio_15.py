#Entradas
PvP=float(input("Ingrese el precio de venta al publico: "))
Pf=float(input("Ingrese el precio final "))
#caja negra
Desc=((Pf-PvP)/PvP)
Desc_2=round((Desc*100), 2)
#Salidas
print(f"el procentaje de descuento aplicado es de: {Desc_2}%" )