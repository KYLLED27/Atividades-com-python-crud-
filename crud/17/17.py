convidados =[]
id_config = 1

def cadastrar():
    global id_config
    nome1 = input("Digite o nome para o cadastro: ")
    convidado = {"id": id_config, "nome": nome1}
    id_config += 1
    convidados.append(convidado)
    print("Convidado cadastrado")
    print(convidados)

while True:
    cadastrar()
    continuar = input("Deseja continuar? s/n ")
    if continuar == "n":
        break
