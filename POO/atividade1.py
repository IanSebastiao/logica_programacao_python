class Aluno:
    def __init__(self,matricula,nome,notas):
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
        

alunos = []

while True:
    notas = []
    nome = input('Digite seu nome: ')
    matricula = input('Digite sua matricula: ')
    nota1 = float(input('Digite sua nota 1: '))
    nota2 = float(input('Digite sua nota 2: '))
    nota3 = float(input('Digite sua nota 3: '))
    notas.append(nota1)
    notas.append(nota2)
    notas.append(nota3)
    aluno = Aluno(nome, matricula, notas)
    aluno.media = sum(aluno.notas) / len(aluno.notas)
    aluno.conceito = aluno.conceito_aluno()
    aluno.resultado = aluno.resultado_aluno()
    alunos.append(aluno)

    s = input('Digite S para sair ou ENTER para continuar: ')

    if s.upper() == 'S':
        break

    

