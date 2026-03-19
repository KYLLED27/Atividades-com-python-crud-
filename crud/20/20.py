convidados = [
    {"nome": "luis", "mesa":5},
    {"nome": "joao", "mesa":5},
    {"nome": "maikel", "mesa":2},
    {"nome": "peola", "mesa":5}
]

mesa_pra_visu = int(input("Digite a mesa para a visualização: "))

for busca in convidados:
    if busca["mesa"] == mesa_pra_visu:
        print(busca["nome"])


