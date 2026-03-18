convidados = [
    {"id": 1.,"nome":"Maria","cpf":"000","mesa":1},
    {"id": 2,"nome":"asdrubal","cpf":"123","mesa":2},
    {"id": 3,"nome":"pedro","cpf":"321","mesa":3}
]

cpf = input("Digite o CPF do convidado: ")

encontrado = False

for deletar in convidados:
    if deletar["cpf"] == cpf:
        convidados.remove(deletar)
        print("Convidado deletado com sucesso")
        encontrado = True
        
for xyz in convidados:
    print(xyz)