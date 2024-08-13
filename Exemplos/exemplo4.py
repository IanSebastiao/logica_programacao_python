'''Sistema que leia duas notas e o nome do aluno
Calcular a média
Mostrar resultado da média
Mostrar se aluno está aporovado (media >=6)
Reprovado (Media <5)
Recuperação (Media >=5 e media <6)'''

nome = input('Digite seu nome:')
nota1 = float(input("Digite sua nota 1:"))
nota2 = float(input("Digite sua nota 2:"))
media = (nota1 + nota2) / 2

print('Nome:', nome)
print('Média: ', media)

if media >= 6:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')     
