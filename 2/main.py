cpf = (input("Consulte seu CPF: ").strip())

if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido. vai ser mesario")
    
else: 
    print("CPF ERRADO BURRO")