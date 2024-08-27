#Tarefa 1 - Faça um programa que peça um número e então mostre a mensagem "o número informado foi..."

'''numero = int(input('digite um núemro'))
print(f'o número informado foi {numero}')'''

#Tafera 2 - Faça um programa que peça o nome, a idade, a altura e o CPF e impra a mensagem 'bem-vindo (usuário), seus dados foram cadastrados com sucesso.'

'''def dadosPessoais():
    nome = input('Digite seu nome')
    altura = float(input('digite sua altura'))
    idade = input('digite sua idade')
    CPF = input('digite seu CPF')
    print(f"Olá! Seja bem-vindo, {nome}. Seus dados foram cadastrados com sucesso! Sua altura é: {altura}m, sua idade é: {idade} anos e seu CPF é: {CPF}")

dadosPessoais()'''

# Tarefa 3 - Faça um programa que peça dois números e impra a soma

'''num1 = int(input('Digite um número'))
num2 = int(input('Digite um número'))
total = {num1 + num2}
print(f'a soma é {total}')'''

# Tarefa 4 - Faça um programa que peça as 4 notas bimestrais e mostra a média

'''def notasBimestrais():
    b1 = int(input('digite a nota do primeiro bimestre'))
    b2 = int(input('digite a nota do segundo bimestre'))
    b3 = int(input('digite a nota do tereceiro bimestre'))
    b4 = int(input('digite a nota do quarto bimestre'))
    media = (b1 + b2 + b3 + b4) / 4
    print(f'a média é {media}')

notasBimestrais()'''

# Tarefa 5 - Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

'''def quadrado():
    base = int(input('Digite o valor da base'))
    altura = int(input('Digite o valor da altura'))
    area = (base*altura)
    print(f'A área do quadrado é {area}cm e o dobro é {area*2}cm ')

quadrado()'''

# Tarefa 6 - Faça um programa que pergunte quanto você ganha por hora e número de horas trabalhadas no mês. Calcule e mostre o total do seu salário

def ganhoPorHora():
    salario = float(input('Quanto você ganha?'))
    horasTrabalhadas = int(input('Quantas horas você trabalha'))
    print(f'Você recebe {horasTrabalhadas/salario}')

ganhoPorHora()


