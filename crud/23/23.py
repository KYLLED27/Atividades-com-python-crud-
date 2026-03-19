lista = [
    {"nome": "luis", "cpf": "123", "chek_in": False},
    {"nome": "perola", "cpf": "321", "chek_in": True},
    {"nome": "ariel", "cpf": "421", "chek_in": False}
]

total_convidados = 0
total_confirmados = 0
total_pendentes = 0

for convidado in lista:
    total_convidados += 1
    if convidado["chek_in"] == True:
        total_confirmados += 1
    else:
        total_pendentes += 1

percentual = (total_confirmados/total_convidados)*100

print(f"Total de convidados: {total_convidados}")
print(f"Total confirmados: {total_confirmados}")
print(f"Total pendentes: {total_pendentes}")
print(f"percentual: {percentual:.2f}%")
