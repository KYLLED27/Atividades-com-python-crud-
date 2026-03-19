ista = [
    {"nome": "luis", "cpf": "123", "chek_in": False},
    {"nome": "perola", "cpf": "", "chek_in": True},
    {"nome": "ariel", "chek_in": False}
]

for convidado in lista:
    if "cpf" not in convidado or convidado["cpf"] == "":
        lista.remove(convidado)

print(lista)