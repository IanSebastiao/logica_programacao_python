from models.funcionario import Funcionario


def funcionario():
    nome = input('Digite seu nome: ')
    sexo = input('Digite seu sexo: ')
    cpf = input('Digite seu CPF: ')
    telefone = input('Digite seu telefone: ')
    email = input('Digite seu email: ')
    matricula = input('Digite sua matricula: ')
    funcao = input('Digite qual a sua funcao: ')
    salario = float(input('Digite qual valor do seu sálario>: '))

    funcionario = Funcionario(nome, sexo, cpf, telefone, email, matricula, funcao, salario)

    return funcionario