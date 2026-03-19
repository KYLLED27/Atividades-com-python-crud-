lista = [
    {"nome": "João"},
    {"nome": "Maria"},
    {"nome": "leandro"}
]

lista_ordenada = sorted(lista, key=lambda x: x['nome'])

nomes_apenas = [pessoa['nome'] for pessoa in lista_ordenada]

print(nomes_apenas)