pg=int(input("ingrese el numero de partidos ganados: "))
pp=int(input("ingrese el numero de partidos perdidos: "))
pe=int(input("ingrese el numero de partidos empatados: "))
pganado=3*pg
pperdido=0*pp
pempatado=1*pe
print("puntos por partidos ganados: ",pganado,"puntos")
print("puntos por partidos perdidos: ", pperdido,"puntos")
print("puntos por partido empatados: ",pempatado,"puntos")
ptotal=int((pg*3)+pe)
print("puntaje total: ",ptotal,"puntos")