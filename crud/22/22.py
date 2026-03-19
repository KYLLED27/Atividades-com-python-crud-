lista = [
    {"nome": "luis", "cpf": "123", "chek_in": False},
    {"nome": "perola", "cpf": "321", "chek_in": True},
    {"nome": "ariel", "cpf": "421", "chek_in": False}
]

def fez_chek():
    for convidado in lista:
        if convidado["chek_in"] == False:
            print(convidado["nome"])

while True:
    fez_chek()
    continuar = input("quer continuar? s/n")
    if continuar.lower() == "n":
        break