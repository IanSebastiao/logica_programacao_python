contador = 0

while True:
    numero = float(input("Digite um número positivo (ou um número negativo para sair): "))
    
    if numero < 0:
        break
    else:
        contador += 1

print("Você digitou", contador ,"números positivos.")
