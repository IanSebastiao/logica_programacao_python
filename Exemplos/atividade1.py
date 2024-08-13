'''sexo = input("Digite seu sexo:")
h = float(input("Digite sua altura:"))

print("Sexo:", sexo)

if sexo == "Masculino":
    print('Seu peso ideal é:', round((72.7*h)-58,2))
else:
    print('Seu peso ideal é:', round((62.1*h) -44.7,2))'''

#Tratamento de erro

try:
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))
    sexo = input('Digite o sexo: ')
except Exception as e:
    print('Houve algum erro', e)
else:
    pesoIdeal = 0.0
    if(sexo.upper() ==  'M'): #lower
        pesoIdeal = round((72.7*altura)-58,2)
    elif(sexo.upper() == 'F'):
        pesoIdeal = round((62.1*altura)-44.7,2)
    else:
        print('O sexo informado deve ser M para masculino ou F para feminino.')

    if(pesoIdeal > 0):
        print('O sexo informado foi: ', sexo.upper())
        print('Seu peso ideal é: ', pesoIdeal)

    imc = float((round((peso/altura**2),2)))

    print('Seu IMC é: ', imc)

    if imc <18.5:
        print('Abaixo do peso')
    elif imc <25:
        print('Peso normal')
    elif imc <30:
        print('Sobrepeso')
    elif imc <35:
        print('Obesidade grau 1')
    elif imc <40:
        print('Obesidade grau 2')
    else:
        print('Obesidade grau 3')
finally:
    print('Fim do programa')