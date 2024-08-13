'''
Pesquisa senac com os alunos: 5
1- Quantidade de alunos do sexo feminino
2- Quantidade de alunos do sexo masculino
3- Média de altura do sexo feminino
4- Média de altura do sexo masculino
5- Aluno com maior altura 
6- Aluno com menor altura
'''

contF = 0
contM = 0
mediaF = 0.0
mediaM = 0.0
maior = 0
menor = 99
for n in range(0,5):
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
        mediaM = mediaM + altura
    else:
        print('Sexo informado é inválido')
        continue

print('A quantidade de alunos do sexo feminino é:', contF)
print('A quantidade de alunos do sexo masculino é:', contM)

if contF > 0:
    mediaF = mediaF/contF

if contM > 0:
    mediaM = mediaM/contM

print('A média de alturas do sexo feminino é:', mediaF)
print('A média de alturas do sexo masculino é:', mediaM)
print('A maior altura é:', maior)
print('A menor altura é:', menor)