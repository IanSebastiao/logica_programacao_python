idade = int(input('Digite sua idade:'))

if idade < 16:
    print("Não eleitor")
elif 18 <= idade <= 65:
    print("Eleitor Obrigatorio")
else:
    print("Eleitor Facultativo")