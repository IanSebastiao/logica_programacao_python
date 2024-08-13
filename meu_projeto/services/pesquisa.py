from meu_projeto.utils import impressao


def pesquisa(produtos):
    print('###### Pesquisa de Produto ######')
    busca = int(input('Digite o codigo do produto que deseja encontrar: '))
    achei = None

    for produto in produtos:
        if busca == produto.codigo:
            achei = produto
            break

    if achei is not None:
        impressao(achei)
    else:
        print('Produto não encontrado')
