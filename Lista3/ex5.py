lista = [1, 2, 3, 4, 2, 2, 5, 6, 2, 7, 8, 9, 2]
numero = int(input('Digite o número que deseja saber: '))

def contar(numero):
    ocorrencias = lista.count(numero)
    return ocorrencias

quantidade = contar(numero)
print(f"O número {numero} aparece {quantidade} vezes na lista.")
