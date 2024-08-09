class Aluno:
    def __init__(self,nome='',matricula='',notas=[]):
        self.matricula = matricula
        self.nome = nome
        self.notas = notas
        self.media = 0
        self.conceito = ''
        self.resultado = ''

    def conceito_aluno(self):
        if self.media >= 9:
            return 'A'
        elif self.media >= 7.5 and self.media < 9:
            return 'B'
        elif self.media >= 6 and self.media < 7.5:
            return 'C'
        elif self.media >= 4 and self.media < 6:
            return 'D'
        else: 
            return 'E'
        
    def resultado_aluno(self):
        if self.conceito == 'A' or self.conceito == 'B' or self.conceito == 'C':
            return 'Aprovado'
        else:
            return 'Reprovado'
        

def impressao(aluno):
    print(f'Aluno: {aluno.nome}')
    print(f'Matricula: {aluno.matricula}')
    print(f'Notas: {aluno.notas}')
    print(f'Média: {round(aluno.media, 1)}')
    print(f'Conceito: {aluno.conceito}')
    print(f'Resultado: {aluno.resultado}')

alunos = []

while True:
    notas = []
    nome = input('Digite seu nome: ')
    matricula = input('Digite sua matricula: ')
    for i in range(3):
        nota = float(input(f'Digite a nota {i+1}: '))
        notas.append(nota)
    aluno = Aluno(nome, matricula, notas)
    aluno.media = sum(aluno.notas) / len(aluno.notas)
    aluno.conceito = aluno.conceito_aluno()
    aluno.resultado = aluno.resultado_aluno()
    alunos.append(aluno)

    s = input('Digite S para sair ou ENTER para continuar: ')

    if s.upper() == 'S':
        break

for aluno in alunos:
    impressao(aluno)
    print('')

busca = input('Digite a matricula do aluno que deseja ver os dados: ')
achei = ''
for aluno in alunos:
    if busca == aluno.matricula:
        achei = aluno
        break

if achei != '':
    impressao(achei)
else:
    print('Matricula não encontrada')


'''
    nota1 = float(input('Digite sua nota 1: '))
    nota2 = float(input('Digite sua nota 2: '))
    nota3 = float(input('Digite sua nota 3: '))
    notas.append(nota1)
    notas.append(nota2)
    notas.append(nota3)
'''