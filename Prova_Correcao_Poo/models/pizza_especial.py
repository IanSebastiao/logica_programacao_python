from pizza import Pizza


class PizzaEspecial(Pizza):
    def __init__(self, nome: str, tamanho: str, adicionais: list):
        super().__init__(nome, tamanho)
        self.adicionais = adicionais


    def calcular_adicional(self):
        preco_adicional = 5
        total = 0
        for item in self.adicionais:
            total += preco_adicional
        
        return total
    
    def detalhes_especiais(self):
        print(f'Adicionais: {self.adicionais}')
        print(f'Preço Adicionais: {self.calcular_adicional()}')


pizza = PizzaEspecial('Calabresa', 'M', ['Cheddar', 'Catupiry']) 
pizza.calcular_preco()
pizza.detalhes()
pizza.detalhes_especiais()
