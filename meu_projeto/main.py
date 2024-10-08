
from services.administracao.cadastro import cadastro
from services.caixa.vendas import venda
from services.caixa.lista import lista
from services.administracao.reajuste import reajuste
from services.caixa.pesquisa import pesquisa
from utils.cadastro_pessoa import cadastro_pessoa
from utils.impressao_dados import impressao_dados
from services.administracao.pesquisa_dados import pesquisa_cliente
from services.administracao.pesquisa_dados import pesquisa_funcionario


def main():
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
                        '\n7 - Para o cadastro do funcionario'
                        '\n8 - Para exibir o cadastro do cliente'
                        '\n9 - Para exibir o cadastro do funcionario: \n'
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
            clientes.append(cadastro_pessoa(1))

        elif opcao == 7: 
            funcionarios.append(cadastro_pessoa(2))

        elif opcao == 8:
            cliente = pesquisa_cliente(clientes)
            if cliente is not None:
                impressao_dados(cliente, 1)
            else:
                print('Cliente não cadastrado!')

        elif opcao == 9:
            funcionario = pesquisa_funcionario(funcionarios)
            if funcionario is not None:
                impressao_dados(funcionarios, 2)
            else:
                print('Cliente não cadastrado!')

        else:
            print('Opção Inválida')


        s = input('Digite S para sair ou ENTER para continuar: ')
        if s.upper() == 'S':
            break 

if __name__ == '__main__':
    main()
