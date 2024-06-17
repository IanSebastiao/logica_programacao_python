maior = 0
menor = 99
for n in range(0,15):
    altura = float(input('Digite sua altura:'))

    if altura > maior:
        maior = altura

    if menor > altura:
        menor = altura

print('A maior altura é:', maior)
print('A menor altura é:', menor)