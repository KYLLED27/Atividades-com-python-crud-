produtos = []
id_couter = 1

def iniciar_menu():
    print("\n ----- menu ----")
    print("1.CADASTRAR PRODUTO")
    print("2.LISTAR PRODUTOS")
    print("3.BUSCAR PRODUTO POR ID")
    print("4.ATUALIZAR PRODUTO")
    print("5.REMOVER")
    print("6.SAIR")

def cadastrar():
    global id_couter
    print("COMEÇANDO CADASTRO..")
    nome = input("DIGITE O NOME DO PRODUTO: ")
    preco = float(input("DIGITE O PREÇO DO PRODUTO: "))
    estoque = input("DIGITE A QUANTIDADE EM ESTOQUE: ")
    produto = {"id": id_couter,"nome": nome, "preco": preco, "estoque": estoque}
    id_couter += 1
    produtos.append(produto)
    print("PRODUTO CADASTRADO")

def listar():
    for lista in produtos:
        print("id =", lista["id"])
        print("nome =", lista["nome"])
        print("preco =", lista["preco"])
        print("estoque =", lista["estoque"])
        print("-" * 20)
        
def buscar():
    busca_input = input("DIGITE O ID DO PRODUTO PARA LOCALIZAR: ")
    for busca in produtos:
        busca["id"] == busca_input
        print("SEU PRODUTO")
        print("NOME", busca["nome"])
        print("PREÇO", busca["preco"])
        print("QUANTIDADE NO ESTOQUE", busca["estoque"])

def atualizar():
    busca_input = input("DIGITE O ID DO PRODUTO PARA ATUALIZAR: ")
    for busca in produtos:
        busca["id"] == busca_input
        novo_nome = input("DIGITE O NOVO NOME: ")
        novo_preco = input("DIGITE O NOVO PREÇO: ")
        nova_qnt_estoque = input("DIGITE A NOVA QNT: ")
        busca["nome"] = novo_nome
        busca["preco"] = novo_preco
        busca["estoque"] = nova_qnt_estoque
        print("PRODUTO ATUALIZADO COM SUCESSO")
        break

def remover():
    busca_input1 = input("DIGITE O ID DO PRODUTO PARA REMOVER: ")
    for deletar in produtos:
        if deletar["id"] == int(busca_input1):
            produtos.remove(deletar)
            print("PRODUTO DELETADO")
            break
            
while True:
    iniciar_menu()
    escolha = input()
    if escolha == "1":
        print("PRONTO PRA CADASTRAR")
        cadastrar()
        
    elif escolha == "2":
        print("LISTA COMPLETA")
        listar()
        
    elif escolha == "3":
        print("BUSQUE SEU PRODUTO")
        buscar()
    elif escolha == "4":
        print("ATUALIZE SEU PRODUTO")
        atualizar()
    elif escolha == "5":
        print("REMOVA SEU PRODUTO")
        remover()
    elif escolha == "6":
        print("SAINDO...")
        break
    else:
        print("nao podi")