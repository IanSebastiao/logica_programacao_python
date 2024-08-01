
preco = float(input('Digite o valor do produto:'))

print('Digite 1 para pagar à vista em dinheiro ou cheque, 10% de desconto')
print('Digite 2 para pagar à vista no cartão de crédito, 15% de desconto')
print('Digite 3 para dividir em 2 vezes, sem juros')
print('Digite 4 para dividir em 3 vezes, com juros de 10%')

pagamento = input('Digite a forma de pagamento:')

if pagamento == '1':
    print('Você irá pagar:', preco - 10/100 * preco)
elif pagamento == '2':
    print('Você irá pagar:', preco - 15/100 * preco)
elif pagamento == '3':
    print('Você irá pagar 2 parcelas de:', preco / 2)
elif pagamento == '4':
    print('Você irá pagar 3 parcelas de', round((preco + 10/100 * preco) / 3, 2))
else:
    print('Forma de pagamento Inválida')
