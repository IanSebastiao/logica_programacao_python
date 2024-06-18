ano_nascimento = int(input('Digite seu ano de nascimento:'))
ano_atual = int(input('Digite o ano atual:'))

if ano_nascimento >0:
    idade = ano_atual - ano_nascimento
    print('A idade da pessoa é', idade , 'anos') 
else:
    print('Ano de nascimento invalido ')