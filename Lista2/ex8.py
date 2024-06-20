idade = int(input('Digite sua idade: '))
contador = 1

for n in range(0,9):
    idade = int(input('Digite sua idade: '))

    if idade >= 18:
        contador = contador + 1
    else:
        continue

print(contador, "São maiores de idade")