# While

'''i = 1

while i < 10:
    i += 1
    print(i)'''

#=====================================

# For

#ex1

nomes = ['Felipe', 'Daniele', 'Deo', 'Cesar', 'Renata']

for nome in nomes:
    print(nome)

#//////////////////////////////////////

# Ex2

canal = 'Refatorando'

for letra in canal:
    print(letra)

#/////////////////////////////////////

#ex3

for index in range(6, 21,2):
    print(index)

# Ex4

for index in range(5):
    if index == 0:
        print('primeira linha')
    else:
        print(f'outra linha {index}')


# Ex5 - lista de lista (teclado numérico)

matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    ['#',0,'*'],
]

for linha in matrix_numeros:
    print('----')
    for coluna in linha:
        print(coluna)

#/////////////////////////////////////

#Ex1 - Imprimindo números de 1 a 10

i = 10

for i in range (1,11):
    print(i)


#/////////////////////////////////////

#Ex2 Somando numeros de uma lista

numeros = [1,78,4,45]
soma = 0

for numero in numeros:
    soma += numero

print(f'a soma é: {soma}')


#/////////////////////////////////////


# Ex3 Contando números pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador_num_par = 0

for numero in numeros:
    if numero % 2 == 0:
        contador_num_par += 1
        
print(f'Numero pares: {contador_num_par}')


#/////////////////////////////////////


# 4 - Multiplicando números de 1 a 5

resultado = 1

for multiplicacao in range(1,6):
    resultado *= multiplicacao

print(f'a multplicação é: {resultado}')


#/////////////////////////////////////


# 5 - Repita a string "Python" 5 vezes

for cobras in range(5):
    print('Python')

#/////////////////////////////////////

#  Dada uma string, imprima cada caractere individualmente.

nome = 'Felipe'

for letra in nome:
    print(letra)


#/////////////////////////////////////

#  Imprima a tabuada de multiplicação do número 3

for i in range(1,11):
    print(f'3x{i} = {3*i}')

