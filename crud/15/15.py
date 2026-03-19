lista = [
    "luis",
    "maria",
    "joao",
    "ana",
    "carlos"
]

busca = input("Digite a parte do nome a ser buscado: ")

busca = [nome for nome in lista if busca in nome]
print(busca)   