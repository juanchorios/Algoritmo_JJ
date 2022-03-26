volar = bool(int(input('¿Puede volar? 1:Si 0:No :')))
humano = bool(int(input('¿Es humano? 1:Si 0:No :')))
mascara = bool(int(input('¿Tiene mascara? 1:Si 0:No :')))

if volar is True and humano is True and mascara is True:
    print('Ironman')
elif volar is True and humano is True and mascara is False:
    print('Captain Marvel')
elif volar is True and humano is False and mascara is True:
    print('Ronan Accuser')
elif volar is True and humano is False and mascara is False:
    print('Vision')
elif volar is False and humano is True and mascara is True:
    print('Spiderman')
elif volar is False and humano is True and mascara is False:
    print('Hulk')
elif volar is False and humano is False and mascara is True:
    print('Black Bolt')
elif volar is False and humano is False and mascara is False:
    print('Thanos')
    
