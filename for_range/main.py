'''for i in range (1, 11):
    print(i,'', end="")''' #end='' deixa todo o resultado na mesma linha


#==========================

'''for i in range (10, 0, -1):
    print(i)'''


#================================


#Soma dos números de 1 a 100

'''soma = 0

for numero in range (1,100):
    soma += numero

print(f'a soma dos números de 1 a 100 é: {soma}')'''

#================================

#Números pares

'''for i in range(0, 21, 2):
    print(i)'''



#==============================

#Contagem Regressiva

'''for i in range(10, 0, -1):
    print(i)

print('fogo!')'''


#================================

#Tabuada

numero = int(input('Digite um numero'))
print(f'Tabuada do {numero}')

for i in range (1, 11):
    resultado =  numero * i
    print(f'{numero} x {i} = {resultado}')