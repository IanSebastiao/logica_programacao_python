produtos=[]
precos=[]
qtdes=[]
total = 0
while True:
    try:
        produto = input('Produto:')
        qtde = int(input('Quantidade:'))
        preco = float(input('Digite o valor do produto:'))
        total = total + qtde * preco

        s = input('Digite S para sair ou ENTER para continuar:')

        produtos.append(produto)
        precos.append(preco)
        qtdes.append(qtde)
    except:
        print('Digite um valor válido')
    finally:
        if s.upper() == 'S':
            break

for n in range(len(produtos)):
    print(f'Item {n+1}: {produtos[n]} - Valor: {precos[n]} - Quantidade: {qtdes[n]}')

print(f'\nValor total: {total}')
print('\nForma de pagamento')
print('Digite 1 para pagar à vista em dinheiro ou cheque, 10% de desconto')
print('Digite 2 para pagar à vista no cartão de crédito, 15% de desconto')
print('Digite 3 para dividir em 2 vezes, sem juros')
print('Digite 4 para dividir em 3 vezes, com juros de 10%')
                                                
pagamento = input('Digite a forma de pagamento:')

if pagamento == '1':
    print('Você irá pagar:', total - 10/100 * total)
elif pagamento == '2':
    print('Você irá pagar:', total - 15/100 * total)
elif pagamento == '3':
    print('Você irá pagar 2 parcelas de:', total / 2)
elif pagamento == '4':
    print('Você irá pagar', round(total + 10/100 * total, 2) ,' em 3 parcelas de', round((total + 10/100 * total) / 3, 2))
else:
    print('Forma de pagamento Inválida')
