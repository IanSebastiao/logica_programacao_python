from models.pizza import Pizza
from models.pizza_especial import PizzaEspecial
from models.pedido import Pedido

# lista_adicionais = ['Bacon', 'Cheddar']
# lista_pizzas = ['Calabresa', 'Napolitana', 'Portuguesa', 'Frango']
# pizzas = []

# print('''
#         Preços: P - 10, M - 20, G - 30'
#         1 - Calabresa
#         2 - Napolitana
#         3 - Portuguesa
#         4 - Frango
# ''')

# op = input('Escolha a pizza: ')
# tamanho = input('Tamanho [P, M, G]: ')
# escolha = input('Deseja algum adicional [S - Sim, N - Não]')
# if escolha.upper() == 'S':
#     while escolha.upper() == 'S':
#         adicional = input('''Informe o adicional:
#                           1 - Cheddar
#                           2 - Bacon
#                           ''')
#         lista_adicionais.append(adicional)
#         escolha = input('Deseja mais algum adicional [S - Sim, N - Não]')
#         pizza = PizzaEspecial(pizzas[op-1], tamanho, lista_adicionais)
#         pizza.calcular_preco()
# else:
#     pizza = Pizza(pizzas[op-1], tamanho)
#     pizza.calcular_preco()



def pizzaria(numero_pedido):

  lista_pizzas = ['Calabresa', 'Portuguesa', 'Napolitana']
  lista_adicionais = ['Muçarela', 'Pimentão', 'Ovo']

  pedido = Pedido(numero_pedido)
  while True:
    adicionais = []
    
    print('''
          Preços: P - 10, M - 20, G - 30
          1- Calabresa
          2- Portuguesa
          3- Napolitana
          ''')
    op = int(input('Escolha a pizza: '))
    tamanho = input('Tamanho [P, M, G]: ')

    escolha = input('Deseja algum adicional [S - Sim, N - Não]?  ')
    if escolha.upper() == 'S':
        while escolha.upper() == 'S':
            adicional = int(input('1- Muçarela\n'
                              '2- Pimentão\n'
                              '3- Ovo\n'
                            'Informe o adicional: '
                              ))
            adicionais.append(lista_adicionais[adicional-1])
            escolha = input('Deseja mais algum adicional [S - Sim, N - Não]?  ')
        pizza = PizzaEspecial(lista_pizzas[op-1], tamanho, adicionais)
        pizza.calcular_preco()
        pedido.adicionar_pizza(pizza)
        
    else:
      pizza = Pizza(lista_pizzas[op-1], tamanho)
      pizza.calcular_preco()
      pedido.adicionar_pizza(pizza)
    
    escolha = input('Deseja adicionar mais algum item no pedido [S - Sim, N - Não]:' )
    if escolha.upper() == 'N':
      break

  pedido.detalhes_pedido()

   