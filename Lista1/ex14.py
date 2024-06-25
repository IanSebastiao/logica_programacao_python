import math

# Essa eu não sabia fazer tive que pesquisar e não entendi '-'

"""def calcular_raizes(a, b, c):
    if a == 0:
        return "Não é equação do segundo grau."
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        return "Não há raízes."
    elif delta == 0:
        raiz = -b / (2*a)
        return f"A equação tem uma raiz: {raiz}"
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return f"As raízes da equação são: {raiz1} e {raiz2}"
"""

# Ler os valores de a, b e c do usuário
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Calcular e exibir o resultado
delta = b**2 - 4*a*c

if delta < 0:
    print(f'Delta: {delta} - Não há raízes')
elif delta == 0:
    print(f'Delta: {delta} - Não é equação do segundo grau')
else:
    raiz1 = (-b + (delta**0.5)) / 2*a

    raiz2 = (-b - (delta**0.5)) / 2*a

    print(f'Delta: {delta} - raiz 1: {raiz1}, raiz 2: {raiz2}')

'''
if a == 0:
    print("Não é equação do segundo grau.")
elif delta <0:
    print("Não há raizes.")
elif delta == 0:
    raiz = -b / (2*a)
    print("A equação tem uma raiz:", raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes da esquação são:", raiz1, raiz2)
'''