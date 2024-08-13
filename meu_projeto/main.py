
from services.cadastro import cadastro
from services.vendas import venda
from services.lista import lista
from services.reajuste import reajuste
from services.pesquisa import pesquisa
from services.cliente import cliente
from services.funcionario import funcionario

    
produtos = []
clientes = []
funcionarios = []

while True:
    opcao = int(input('Escolha a opção desejada'
                    '\n1 - Para cadastrar produto'
                    '\n2 - Para pesquisar produto'
                    '\n3 - Para impressão da lista de produtos'
                    '\n4 - Para venda do produto' 
                    '\n5 - Para reajuste '
                    '\n6 - Para o cadastro do cliente '
                    '\n7 - Para o cadastro do funcionario '
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

    elif opcao == 6: 
        clientes.append(cliente())

    elif opcao == 7: 
        funcionarios.append(funcionario())

    else:
        print('Opção Inválida')


    s = input('Digite S para sair ou ENTER para continuar: ')
    if s.upper() == 'S':
        break

