convidados = [
    {"nome": "Luis", "cpf": "123", "mesa": "1"}
]

def busca():
    cpf = input("Digite o cpf do convidado: ")
    encontrado = False
    
    for convidado in convidados:
        if convidado["cpf"] == cpf:
            print("CONVIDADO ENCONTRADO")
            encontrado = True
            mesa_nova = input("Digite a mesa nova: ")
            convidado["mesa"] = mesa_nova
            break  
    
    if not encontrado:
        print("NAO ENCONTRADO")

while True:
    busca()
    continuar = input("Continuar? s/n: ")
    if continuar.lower() == "n":
        break