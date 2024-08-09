class Produto:
    def __init__(self, nome: str, codigo: str, preco: float, quantidade: int):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade

    def desconto(self, percentual: float):
        return self.preco - self.preco * percentual / 100
    
    def reajuste(self, percentual: float):
        return self.preco + self.preco * percentual / 100




def impressao(produto):
    print(f'Produto: {produto.nome}')
    print(f'Codigo do produto: {produto.codigo}')
    print(f'Preço do produto: {produto.preco}')
    print(f'Quantidade de produtos: {produto.quantidade}')

def cadastro():
    nome = input(('Nome do produto: '))
    codigo = int(input('Digite o código do produto: '))
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite a quantidade do produto: '))
    
    produto = Produto(nome, codigo, preco, quantidade)

    return produto

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

def lista(produtos):
    print('\n ###### Lista de Produtos ######')
    for produto in produtos:
        impressao(produto)
        print('')

def venda(produtos):
    print('###### Venda de Produto ######')
    busca = int(input('Digite o codigo do produto: '))
    perc = float(input('Digite o percentual do desconto: '))
    achei = None
    valor_desconto = 0.0

    for produto in produtos:
        if busca == produto.codigo:
            achei = produto
            valor_desconto = produto.desconto(perc)
            produto.preco = valor_desconto
            break

    if achei is not None:
        impressao(achei)
    else:
        print('Produto não encontrado')

def reajuste(produtos):
    print('###### Reajuste de Produto ######')
    busca = int(input('Digite o codigo do produto: '))
    perc = float(input('Digite o percentual do aumento: '))
    achei = None
    preco_reajustado = 0.0

    for produto in produtos:
        if busca == produto.codigo:
            achei = produto
            preco_reajustado = produto.reajuste(perc)
            produto.preco = preco_reajustado
            break

    if achei is not None:
        impressao(achei)
    else:
        print('Produto não encontrado')
    
produtos = []

while True:
    opcao = int(input('Escolha a opção desejada'
                    '\n1 - Para cadastrar produto'
                    '\n2 - Para pesquisar produto'
                    '\n3 - Para impressão da lista de produtos'
                    '\n4 - Para venda do produto' 
                    '\n5 - Para reajuste'
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
