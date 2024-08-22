class Pizza:
    def __init__(self, nome: str, tamanho: str):
        self.nome = nome
        self.tamanho = tamanho
        self.preco = 0

    def calcular_preco(self):
        tamanho_preco = {
            'P' : 10,
            'M' : 20,
            'G' : 30
        }
        self.preco = tamanho_preco.get(self.tamanho, 1.)
        '''for tamanho in tamanho_preco.keys:
            if tamanho == self.tamanho:
                self.preco = tamanho_preco[tamanho]
                break'''

    def detalhes(self):
        print(f'Nome: {self.nome}')
        print(f'Tamanho: {self.tamanho}')
        print(f'Preço Pizza: {self.preco}')

# pizza = Pizza('Calabresa', 'M')
# pizza.calcular_preco()
# pizza.detalhes()