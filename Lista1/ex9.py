sigla_estado = input("Digite a sigla do seu estado (ex: RJ, SP, MG, GO): ")

if sigla_estado == "RJ":
    print("Você é: Carioca")
    
elif sigla_estado == "SP":
    print("Você é: Paulista")
    
elif sigla_estado == "MG":
    print("Você é: Mineiro")
    
elif sigla_estado == "GO":
    print("Você é: Goiano")
else:
    print("Você é de outro estado")