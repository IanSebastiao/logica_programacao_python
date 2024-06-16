numero = int(input("Digite um numero e descubra se ele é multiplo de 3: "))

def multiplo_3(numero):
    return numero % 3 == 0

if multiplo_3(numero):
    print(numero ,"É multiplo de 3")
else:
    print(numero ,"Não é multiplo de 3")