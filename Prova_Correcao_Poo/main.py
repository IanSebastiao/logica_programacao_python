from models.pizza import Pizza
from models.pizza_especial import PizzaEspecial
from models.pedido import Pedido

lista_adicionais = ['Bacon', 'Cheddar']
lista_pizzas = ['Calabresa', 'Napolitana', 'Portuguesa', 'Frango']
pizzas = []

print('''
        Preços: P - 10, M - 20, G - 30'
        1 - Calabresa
        2 - Napolitana
        3 - Portuguesa
        4 - Frango
''')

op = input('Escolha a pizza: ')
tamanho = input('Tamanho [P, M, G]: ')
escolha = input('Deseja algum adicional [S - Sim, N - Não]')
if escolha.upper() == 'S':
    while escolha.upper() == 'S':
        adicional = input('''Informe o adicional:
                          1 - Cheddar
                          2 - Bacon
                          ''')
        lista_adicionais.append(adicional)
        escolha = input('Deseja mais algum adicional [S - Sim, N - Não]')
else:
    pizza = Pizza(pizzas[op-1], tamanho)
    pizza.calcular_preco()