from datetime import date
ano = int(input("Qual seu ano de nascimento?:"))
sexo = str(input("Qual seu sexo?(M/F):").upper().strip(" "))
ida = date.today().year-ano
print(f"Esse ano é o ano dos seus {ida} anos.")

if ida >= 18 and sexo == "M":
    print("""Você deve se alistar, ou deve já ter sido alistado 
e acompanhar ou ter acompanhado seu alistamento.""")
elif sexo == "F":
    print("""Você não precisa se alistar, 
mas caso queira, vá até o Centro de Alistamento 
mais próximo, ou pelo site.""")
else:
    print("Você ainda não precisa se alistar.")