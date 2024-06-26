numero = int(input('Digite o número no qual deseja saber a tabuada: '))

def tabuada(numero):
    print(f'Tabuada do número: {numero}')
    for t in range(1,11):
        print(f'{numero} x {t} = {numero * t}')

tabuada(numero) 