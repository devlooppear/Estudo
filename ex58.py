from random import randint
com = randint(1,11)
som = 0
print("""Sou o seu computer, tô pensando em um número de 0 a 10.
Advinha ae, se você é o bom. Manda pô pai""")
palpite = -1
while palpite != com:
    som = som+1
    palpite = int(input("Qual número?:"))
    if palpite == com:
        print(f"ACERTOUU! Com {som} tentativas!")
        break
