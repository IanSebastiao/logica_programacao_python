q = []
p = []
total = 0
vendas = int(input('Digite a quantidade de vendas: '))

for n in range(vendas):
    quant = int(input('Digite a quantidade do produto: '))
    q.append(quant)
    preco = float(input('Digite o preço do produto: '))
    p.append(preco)
    total += quant * preco
print(f'Lista das quantidades: {q}')
print(f'Lista dos preçõs: {p}')

print(f'Faturamento mensal: {total}')