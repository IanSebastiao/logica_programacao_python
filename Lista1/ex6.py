numero = int(input('Digite seu número:'))

def divisivel_3_7 (numero):
    return numero % 3 == 0 and numero % 7 == 0 

if divisivel_3_7(numero):
    print('Este numero e divisivel de 3 e 7')
else:
    print('Este numero não é divisivel de 3 e 7')