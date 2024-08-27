#LISTA - Uso de colchetes - é uma coleção ordenadas e mutáveis.Permite membros duplicados

lista = ['Felipe', 'Daniele', 'Gonzaga']
print(lista)

for lista in lista:
    print(lista)


print('-'*30)

#TUPLAS - Uso de parênteses () - é uma coleção ordenadas e imutáveis. Permite membros duplicados

tuplas = ('carro', 'moto', 3.5, 6)
print(tuplas)

for tuplas in tuplas:
    print(tuplas)

print('-'*30)

#DICIONÁRIO - Uso de chaves + valor {} - é uma coleção ordenada e mutável. Nenhum membro duplicado

dicionario = {'nome': 'Felipe', 'Logica': True, 'numero': 2, 'outro numero': 3.5}
print(dicionario)
print(type(dicionario))

print('-'*30)

#CONJUNTO - é uma coleção não ordenada e não indexada. Nenhum membro duplicado

conjunto = {'carro', True, 2, 3.5}
print(conjunto)
print(type(conjunto))

print('-'*30)

numero = [1, 2, 3, 4, 5]
print(numero)


print('-'*30)

palestrantes = (
    ('Felipe', 'Palestra sobre Python', 'UNIFOR'),
    ('Daniele', 'Palestra sobre JavaScript', 'Infinity'),
    ('Gonzaga', 'Palestra sobre C++', 'Estácio')
    )
nome, tema, instituicao = palestrantes[1]
print(f'Nome: {nome}\nTema da Palestra: {tema}\nInstituicao {instituicao}')

print('-'*30)


'''Suponha que você está gerenciando uma competição esportiva e tem
uma lista de tuplas representando os resultados das equipes em
diferentes modalidades. Cada tupla contém o nome da equipe, seguido
por uma lista de pontuações obtidas em cada rodada da competição.

1.Calcule a média das pontuações de cada equipe e armazene esses
valores em uma nova lista chamada medias.
2.Ordene a lista medias em ordem decrescente sem usar lambda
3. Crie uma nova lista chamada classificacao que contém tuplas, onde
cada tupla contém o nome da equipe e sua média de pontuações.'''


resultado = (
    ('Time 1', [85, 90, 58, 95]),
    ('Time 2', [95, 38, 68, 85]),
    ('Time 3', [60, 98, 58, 100]),
    ('Time 4', [85, 70, 98, 48])
)

medias = []

for equipes, pontuacao in resultado:
    media = sum(pontuacao) / len(pontuacao)
    medias.append((equipes, media))

print(medias)

classificacao = []

for equipe, pontuacao in resultado:
    media = sum(pontuacao) / len(pontuacao)
    classificacao.append((equipe, media))

print(classificacao)