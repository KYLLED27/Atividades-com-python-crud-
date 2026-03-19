
convidados = [
    {"nome": "maria", "cpf": "123","checking": False}
]
def contagem():
    print(len(convidados))

    

def cadastrar():
    nome=input("digite seu nome: ")
    cpf=input("digite seu cpf: ")
    convidado = {"nome": nome, "cpf": cpf}
    convidados.append(convidado)     
def listar():
    print(convidados)
def buscar():
    cpf=input("Digite o CPF do convidado: ")
    encontrado = False
    for busca in convidados:
        if busca["cpf"] == cpf:
            print(busca)
            encontrado = True
    if not encontrado:
        print("convidado nao encontrado")  
        
def editar():
    cpf = input("Digite o cpf do convidado para editar: ")
    encontrado = False
    for edita in convidados:
        if edita["cpf"] == cpf:
            novo=input("Digite o novo nome: ")
            edita["nome"] = novo
            print("novo nome cadastrado")
            encontrado = True
def remover():
    cpf2 = input("Digite o CPF do convidado: ")
    encontrado = False
    for deletar in convidados:
        if deletar["cpf"] == cpf2:
            convidados.remove(deletar)
            print("Convidado deletado com sucesso")
            encontrado = True
            break
    if not encontrado:
        print("Convidado não encontrado")

def fazer():
    cpf3 = input("Digite o CPF para checkin: ")
    encontrado = False
    for check in convidados:
        if check["cpf"] == cpf3:
            if check.get("checkin"):
                print("Checkin já feito")
            else:
                check["checkin"] = True
                print("Checkin feito com sucesso")
            encontrado = True
            break
    if not encontrado:
        print("Convidado não encontrado")

def mostrar():
    print("Lista de convidados:")
    print(convidados)

def exibir_menu():
        print("\n---   MENU   ---")
        print("1.Cadastrar")
        print("2.Listar")
        print("3.buscar")
        print("4.editar")
        print("5.remover")
        print("6.Fazer Checkin")
        print("7.mostrar relatorios")
        print("8.sair")
    
while True:
    exibir_menu()
    opcao = input("escolha uma opção: ")
    if opcao == "1":
        cadastrar()
        print()
    elif opcao == "2":
        listar()
        print()
    elif opcao == "3":
        buscar()
        print()
    elif opcao == "4":
        editar()
        print()
    elif opcao == "5":
        print("Executando remover()...")
        remover()
    elif opcao == "6":
        fazer()
        print()
    elif opcao == "7":
        contagem()
        print()
    elif opcao == "8":
        print("vc saiu")
        break
    else:
        print("opção invalida")
    
    