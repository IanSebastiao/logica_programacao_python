'''
Algoritimo que armazena uma lista de nomes. o usuario deve digitar os nomes até que seja informado o valor -1.
Mostrar o número de pessoas
Printar a lista em ordem alfabetica
Printar o 3º elemento da lista
Realizar sorteio e mostrar nome do ganhador
'''

'''nomes = []

while True: 
    nome = input('Digite seu nome ou -1 para parar: ')
    
    if nome == "-1":
        break

    else:
        nomes.append(nome)

n = len(nomes)
print(f'A quantidade de pessoas é: {n}')

a = sorted(nomes)
print(f'A lista em ordem alfabetica é: {a}')

if nomes >= 3:
    print(f'O terceiro nome da lista é: {nomes[2]}')'''

import random

nomes = []

while True:
    nome = input('Digite um nome:')
    if nome == '-1':
        break
    else:
        nomes.append(nome)

ordem = sorted(nomes)

print(f'Número de pessoas: {len(nomes)}')
print(f'Lista de nomes: {nomes}')
print(f'Lista de nomes em ordem alfabetica: {ordem}')
print(f'O terceiro nome informado é: {nomes[2]}')

random.seed()
sorteado = random.randint(0, len(nomes)-1)
print(f'O nome sorteado foi: {nomes[sorteado]}')
