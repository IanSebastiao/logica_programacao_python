from services import impressao


def lista(produtos):
    print('\n ###### Lista de Produtos ######')
    for produto in produtos:
        impressao(produto)
        print('')