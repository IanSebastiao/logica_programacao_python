from models.cliente import Cliente


def cliente():
    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo: ')
    cpf = input('Digite seu CPF: ')
    telefone = input('Digite seu telefone: ')
    email = input('Digite seu email: ')
    endereco = input('Digite seu endereço: ')

    cliente = Cliente(nome, sexo, cpf, telefone, email, endereco)

    return cliente