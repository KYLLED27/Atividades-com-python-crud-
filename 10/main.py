import time

convidados = {
        "CPF " : "04883962040",
        "check" : False 
}

def fazer_check():
    if convidados["check"] == True:
        print("seu chek foi realizado anteriormente")
    else:
        convidados["check"] = True
        print("seu check foi realizado")

fazer_check()

time.sleep(1)

fazer_check()