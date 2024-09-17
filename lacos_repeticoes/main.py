# While

'''i = 1

while i < 10:
    i += 1
    print(i)'''

#=====================================

# For

#ex1

# nomes = ['Felipe', 'Daniele', 'Deo', 'Cesar', 'Renata']

# for nome in nomes:
#     print(nome)

#//////////////////////////////////////

#Ex2

# canal = 'Refatorando'

# for letra in canal:
#     print(letra)

#/////////////////////////////////////

#ex3

# for index in range(6, 21,2):
#     print(index)

# Ex4

# for index in range(5):
#     if index == 0:
#         print('primeira linha')
#     else:
#         print(f'outra linha {index}')


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