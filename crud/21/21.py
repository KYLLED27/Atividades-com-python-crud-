lista = [
    {"nome": "luis", "cpf": "123", "chek-in": False},
    {"nome": "perola", "cpf": "321", "chek-in": False},
    {"nome": "ariel", "cpf": "421", "chek-in": False}
]

def fazer_chek():
    cpf = input("digite o cpf para o check-in: ")
    encontrado = False

    for convidado in lista:
        if convidado["cpf"] == cpf:
            print("ENCONTREI")
            convidado["chek-in"] = True
            print(lista)
            break
        if not convidado["cpf"] == cpf:
          print("NAO ENCONTREI")

while True:
    fazer_chek()
    continuar = input("quer continuar? s/n")
    if continuar.lower() == "n":
        break
