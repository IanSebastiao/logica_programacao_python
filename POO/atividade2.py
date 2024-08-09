class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade


def impressao(produto):
    print(f'Produto: {produto.nome}')
    print(f'Codigo do produto: {produto.codigo}')
    print(f'Preço do produto: {produto.preco}')
    print(f'Quantidade de produtos: {produto.quantidade}')

produtos = []

while True:
    nome = input(('Nome do produto: '))
    codigo = int(input('Digite o código do produto: '))
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite a quantidade do produto: '))
    produto = Produto(nome, codigo, preco, quantidade)
    produtos.append(produto)

    s = input('Digite S para sair ou ENTER para continuar: ')

    if s.upper() == 'S':
        break


for produto in produtos:
    impressao(produto)
    print('')

busca = int(input('Digite o codigo do produto que deseja encontrar: '))
achei = ''

for produto in produtos:
    if busca == produto.codigo:
        achei = produto
        break

if achei != '':
    impressao(achei)
else:
    print('Produto não encontrado')