from pizza import Pizza


class Pedido():
    def __init__(self, numero_pedido: int):
        self.pizzas = []
        self.numero_pedido = numero_pedido

    def adicionar_pizza(self, pizza):
        self.pizzas.append(pizza)

    def total_pedido(self):
        total = 0
        for pizza in self.pizzas:
            total += pizza.preco

        return total
    
    def detalhes_pedido(self):
        print(f'Total: {self.total_pedido()}')
    
pizza1 = Pizza('Calabresa', 'M')
pizza1.calcular_preco()
pizza2 = Pizza('Frango', 'G')
pizza2.calcular_preco()
p = Pedido(1001)
p.adicionar_pizza(pizza1)
p.adicionar_pizza(pizza2)

for pizza in p.pizzas:
    pizza.detalhes()

p.detalhes_pedido()