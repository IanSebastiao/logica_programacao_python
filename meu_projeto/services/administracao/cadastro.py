from models.produto import Produto


def cadastro():
    nome = input(('Nome do produto: '))
    codigo = int(input('Digite o código do produto: '))
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite a quantidade do produto: '))
    
    produto = Produto(nome, codigo, preco, quantidade)

    return produto