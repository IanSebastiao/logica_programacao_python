idades = 0
pessoas = 0

while True:
    idade = int(input("Digite a idade (ou 0 para finalizar): "))

    if idade == 0:
        break
    
    idades += idade
    pessoas += 1

if pessoas == 0:
    print("Nenhuma idade válida foi inserida.")
else:
    media_idades = round(idades / pessoas,2)
    print("A idade média do grupo de indivíduos é: ", media_idades)
