ano_nascimento = int(input('Digite seu ano de nascimento:'))
ano_atual = int(input('Digite o ano atual:'))

def calcular_idade (ano_nascimento, ano_atual):
    if ano_nascimento > ano_atual:
        return None
    return ano_atual - ano_nascimento

idade = calcular_idade(ano_nascimento, ano_atual)

if idade is not None:
    print('A idade da pessoa é', idade , 'anos')

else:
    print('Ano de nascimento invalido ')