numero = int(input('Digite seu número:'))

def entre_20_90 (numero):
    return 20 <= numero <=90

if entre_20_90 (numero):
    print('Seu número está entre 20 e 90')

else:
    print('Seu número não está entre 20 e 90')