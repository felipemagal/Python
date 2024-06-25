def numero():
    var = int(input('digite um número'))
    if var < 0:
        print(f'O número {var} é negativo')
    elif var == 0:
        print(f'O número {var} é igual a zero')
    else:
        print(f'O número {var} é positivo')

numero()