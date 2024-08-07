'''class Aluno:
    nome = ''
    matricula = ''
    notas = []
    conceito = ''
    media = 0
    resultado = ''

    def conceito_aluno(self):
        if self.media >= 90:
            self.conceito = 'A'
        elif self.media >= 75 and self.media < 90:
            self.conceito = 'B'
        elif self.media >= 60 and self.media < 75:
            self.conceito = 'C'
        elif self.media >= 40 and self.media < 60:
            self.conceito = 'D'
        else: 
            self.conceito ='E'

aluno1 = Aluno()
aluno1.nome = 'Ian'
aluno1.matricula = '810703'
aluno1.notas = [8, 7, 9]

aluno1.media = sum(aluno1.notas) / len(aluno1.notas)

aluno1.conceito = aluno1.conceito_aluno()

print(f'Matricula: {aluno1.matricula}')
print(f'Aluno: {aluno1.nome}')
print(f'Notas: {aluno1.notas}')
print(f'Média: {round(aluno1.media, 1)}')
print(f'Conceito: {aluno1.conceito}')
'''


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
        
def impressao(aluno):
    print(f'Matricula: {aluno.matricula}')
    print(f'Aluno: {aluno.nome}')
    print(f'Notas: {aluno.notas}')
    print(f'Média: {round(aluno.media, 1)}')
    print(f'Conceito: {aluno.conceito}')
    print(f'Resultado: {aluno.resultado}')

aluno1 = Aluno('810703', 'Ian', [10, 10, 10])
aluno1.media = sum(aluno1.notas) / len(aluno1.notas)
aluno1.conceito = aluno1.conceito_aluno()
aluno1.resultado = aluno1.resultado_aluno()

aluno2 = Aluno('810704', 'Gabriel', [2, 3, 1])
aluno2.media = sum(aluno2.notas) / len(aluno2.notas)
aluno2.conceito = aluno2.conceito_aluno()
aluno2.resultado = aluno2.resultado_aluno()

impressao(aluno1)
print('')
impressao(aluno2)
