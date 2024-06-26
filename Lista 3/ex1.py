numeros = []
indice = 1
numero = int(input('Digite um número: '))
numeros.append(numero)
maior = numero
for n in range(2,11):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if maior < numero:
        maior = numero
        indice = n
print(f'Lista dos números: {numeros}')
print(f'Maior número: {maior} - seu índicie é: {indice}')