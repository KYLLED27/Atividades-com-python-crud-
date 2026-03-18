chek = False
convidados = [
    {"id": 1.,"nome":"Maria","cpf":"000","mesa":1 , "check": False},
    {"id": 2,"nome":"asdrubal","cpf":"123","mesa":2, "check": False},
    {"id": 3,"nome":"pedro","cpf":"321","mesa":3 , "check": False}
]

cpf = input("Digite o CPF do convidado: ")

for chek in convidados:
    if chek["cpf"] == cpf:
        print("Check feito com sucesso")
        chek["check"] = True
        break
        
