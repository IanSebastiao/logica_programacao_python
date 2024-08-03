def conceito(ma):
    if ma >= 90:
        return 'A'
    elif ma >= 75 and ma < 90:
        return 'B'
    elif ma >= 60 and ma < 75:
        return 'C'
    elif ma >= 40 and ma < 60:
        return 'D'
    else: 
        return 'E'

def final(conceito):
    if conceito == 'A' or conceito == 'B' or conceito == 'C':
        return 'Aprovado'
    else:
        return 'Reprovado'

try:
    matricula = int(input('Digite sua matricula:'))
    nota1 = float(input('Digite sua nota1:'))
    nota2 = float(input('Digite sua nota2:'))
    nota3 = float(input('Digite sua nota3:'))
    me = float(input('Digite a média dos exercícios:'))
    ma = round((nota1 + nota2 *2 + nota3 * 3 + me) /7, 2)

    print(f'Sua matricula é: {matricula}')
    print(f'Suas notas são: {nota1} - {nota2} - {nota3}')
    print(f'A média de exercicios é de: {me}')
    print(f'A média de aproveitamento é de: {ma}')
    print(f'Seu conceito é: {conceito(ma)}')
    print(f'Você está {final(conceito(ma))}')

except Exception as e:
    print(f'Ocorreu o seguinte erro: {e}')

'''
if ma >= 90:
    conceito = 'A'
elif ma >= 75 and ma < 90:
    conceito = 'B'
elif ma >= 60 and ma < 75:
    conceito = 'C'
elif ma >= 40 and ma < 60:
    conceito = 'D'
else: 
    conceito = 'E'

if conceito == 'A':
    final = 'Aprovado'
elif conceito == 'B':
    final = 'Aprovado'
elif conceito == 'C':
    final = 'Aprovado'
elif conceito == 'D':
    final = 'Reprovado'
elif conceito == 'E':
    final = 'Reprovado'


def final(conceito):
    if conceito == 'A':
        return 'Aprovado'
    elif conceito == 'B':
        return 'Aprovado'
    elif conceito == 'C':
        return 'Aprovado'
    elif conceito == 'D':
        return 'Reprovado'
    elif conceito == 'E':
        return 'Reprovado'
'''