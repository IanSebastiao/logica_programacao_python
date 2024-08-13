from utils.impressao import impressao


def reajuste(produtos):
    print('###### Reajuste de Produto ######')
    busca = int(input('Digite o codigo do produto: '))
    perc = None
    quant = 0
    achei = None
    valor_reajuste = 0.0

    for produto in produtos:
        if busca == produto.codigo:
            achei = produto
            perc = float(input('Digite o percentual do aumento: '))
            valor_reajuste = produto.reajuste(perc)
            produto.preco = valor_reajuste
 
            break

    if achei is not None:
        impressao(achei)
        print(f'Preço com desconto: {valor_reajuste}')
        print(f'Total: {valor_reajuste * quant}')
        print()
    else:
        print('Produto não encontrado')
