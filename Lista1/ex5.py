numero = int(input("Digite um numero e descubra se ele é multiplo de 3: "))

def multiplo_5(numero):
    return numero % 5 == 0

if multiplo_5(numero):
    print(numero ,"É multiplo de 5")
else:
    print(numero ,"Não é multiplo de 5")