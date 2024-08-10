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