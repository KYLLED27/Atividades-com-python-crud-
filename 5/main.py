convidados = []

while True:
    nome = input("Nome ou digite sair: ")
    if nome == "sair":
        break
    
    cpf = input("cpf: ")
    
    convidado = {"nome": nome, "cpf": cpf}
    convidados.append(convidado)

print(convidados)