convidados = [
    {"nome": "luis", "cpf": "12345",
    "nome": "perola", "cpf": "123"}
]

def cadastrar():
  while True:
    nome1 = input("Digite o Nome para cadastro (ou 'sair' para encerrar): ")
    if nome1.lower() == 'sair':
        break
        
    cpf1 = input("Digite o CPF para cadastro: ")

    if any(c["cpf"] == cpf1 for c in convidados):
        print("Erro: CPF já cadastrado! Tente novamente.")

    else:
        convidado = {"nome": nome1, "cpf": cpf1}
        convidados.append(convidado)
        print("Convidado cadastrado com sucesso!")

cadastrar()       