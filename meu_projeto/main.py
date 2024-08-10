
from services import cadastro, lista, pesquisa, reajuste
from services.vendas import venda

    
produtos = []

while True:
    opcao = int(input('Escolha a opção desejada'
                    '\n1 - Para cadastrar produto'
                    '\n2 - Para pesquisar produto'
                    '\n3 - Para impressão da lista de produtos'
                    '\n4 - Para venda do produto' 
                    '\n5 - Para reajuste: '
                    ))

    if opcao == 1:
        produtos.append(cadastro())

    elif opcao == 2:
        pesquisa(produtos)

    elif opcao == 3:
        lista(produtos)

    elif opcao == 4: 
        venda(produtos)

    elif opcao == 5: 
        reajuste(produtos)

    else:
        print('Opção Inválida')


    s = input('Digite S para sair ou ENTER para continuar: ')
    if s.upper() == 'S':
        break

