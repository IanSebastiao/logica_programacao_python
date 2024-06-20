
candidato1 = 0
candidato2 = 0
candidato3 = 0
brancos = 0
nulos = 0
total = 0

while True:
    voto = int(input("Digite o voto (1, 2, 3 para candidatos; 0 para branco; 4 para nulo; -1 para finalizar): "))
    
    if voto == -1:
        break
    
    total += 1
    
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 0:
        brancos += 1
    elif voto == 4:
        nulos += 1
    else:
        print("Voto inválido, por favor digite um voto válido.")

if candidato1 > candidato2 and candidato1 > candidato3:
    vencedor = "Candidato 1"
elif candidato2 > candidato1 and candidato2 > candidato3:
    vencedor = "Candidato 2"
else:
    vencedor = "Candidato 3"

# Exibindo os resultados
print("Número do candidato vencedor: ",vencedor)
print("Número de votos em branco: ", brancos)
print("Número de votos nulos: ", nulos)
print("Número de eleitores que compareceram às urnas: ", total)
