convidados = [
    {"nome": "maria", "cpf": "123"}
]

def cadastrar():
    nome=input("digite seu nome: ")
    cpf=input("digite seu cpf: ")
    convidado = {"nome": nome, "cpf": cpf}
    convidados.append(convidado)     
def listar():
    print(convidados)
def buscar():
    cpf1=input("Digite o CPF do convidado: ")
    encontrado = False
    for busca in convidados:
        if busca["cpf"] == cpf1:
            print(busca)
            encontrado = True
    if not encontrado:
        print("convidado nao encontrado")  
        
def editar():
#def remover
#def fazer
#def mostrar

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
    opção=input("escolha uma opção: ")
    if opção == "1":
        cadastrar()
        print()
    elif opção == "2":
        listar()
        print()
    elif opção == "3":
        buscar()
        print()
    elif opção == "4":
        editar()
        print()
    elif opção == "5":
        remover()
        print()
    elif opção == "6":
        fazer()
        print()
    elif opção == "7":
        mostrar()
        print()
    elif opção == "8":
        print("vc saiu")
        break
    else:
        print("opção invalida")
    