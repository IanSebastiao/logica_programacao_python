from meu_projeto.utils import impressao


def venda(produtos):
    print('###### Venda de Produto ######')
    busca = int(input('Digite o codigo do produto: '))
    perc = None
    quant = 0
    achei = None
    estoque = True
    valor_desconto = 0.0

    for produto in produtos:
        if busca == produto.codigo:
            achei = produto
            quant = int(input('Digite a quantidade: '))
            if quant > produto.quantidade:
                estoque = False
                break
            produto.quantidade -= quant 
            perc = float(input('Digite o percentual do desconto: '))
            valor_desconto = produto.desconto(perc)

            break

    if achei is not None and estoque:
        impressao(achei)
        print(f'Preço com desconto: {valor_desconto}')
        print(f'Total: {valor_desconto * quant}')
        print()
    elif not estoque:
        print(f'Estoque insuficiente: {produto.quantidade}')
    else:
        print('Produto não encontrado')