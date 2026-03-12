name = input("Nome: ")
cpf = input("CPF: ")
mesa = input("Mesa: ")

if len(name) < 3:
    print("O nome deve conter pelo menos 3 caracteres.")

if len(cpf) < 11 or not cpf.isdigit():
    print("O CPF deve conter pelo menos 11 caracteres e ser composto apenas por números.")

print("NOME:", name)
print("CPF:", cpf)
print("MESA:", mesa)