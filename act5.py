palabra=str(input("inserte una palabra: "))
plb=len(palabra)
a=palabra. count('a')
e=palabra. count('e')
i=palabra. count('i')
o=palabra. count('o')
u=palabra. count('u')
mtr=plb*(a+e+i+o+u)
print(f"total de vocales: {mtr}")