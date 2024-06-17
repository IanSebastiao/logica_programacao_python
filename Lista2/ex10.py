
contF = 0
contM = 0
mediaF = 0.0
maior = 0
menor = 99
for n in range(0,3):
    sexo = input('Digite seu sexo:')
    altura = float(input('Digite sua altura:'))

    if altura > maior:
        maior = altura

    if menor > altura:
        menor = altura

    if sexo.upper() == 'F':
        contF = contF + 1
        mediaF = mediaF + altura
    elif sexo.upper() == 'M':
        contM = contM + 1
    else:
        print('Sexo informado é inválido')
        continue

if contF > 0:
    mediaF = mediaF/contF


print('A maior altura é:', maior)
print('A menor altura é:', menor)
print('A quantidade de pessoas do sexo masculino é:', contM)
print('A média de alturas do sexo feminino é:', mediaF)
