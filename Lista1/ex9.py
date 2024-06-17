sigla_estado = input("Digite a sigla do seu estado (ex: RJ, SP, MG, GO): ")

def verificar_estado(sigla):
    sigla = sigla.upper() 
    if sigla == "RJ":
        return "Carioca"
    elif sigla == "SP":
        return "Paulista"
    elif sigla == "MG":
        return "Mineiro"
    elif sigla == 'GO':
        return 'Goiano'
    else:
        return "outro estado"

mensagem = verificar_estado(sigla_estado)
print("Você é", mensagem)