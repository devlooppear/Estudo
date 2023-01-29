from os import system
from random import randint
def Jogo_Par_Impar():
    print(f"{'=-'*20}\nVAMOS JOGAR PAR OU ÍMPAR\n{'=-'*20}")
    com = randint(1,10)
    user = int(input("Digite um valor: "))
    vlr = str(input("Par ou ímpar?[P/I]: ").upper())
    total = user + com
    resultado = ""
    if total % 2 == 0:
        resultado = "DEU PAR"
    else:
        resultado = "DEU ÍMPAR"
    print(f"{'-'*60}\nVocê jogou {user} e o computador {com}. Com o total de {total} {resultado}\n{'-'*60}")
    if vlr == "P" and total % 2 == 0:
        input(f"VOCÊ VENCEU!\nVamos jogar novamente...\n{'=-'*20}\n")
        if True:
            system("cls")
            return Jogo_Par_Impar()
    elif vlr == "P" and total % 2 != 0:
        input(f"VOCÊ PERDEU!\nVamos jogar novamente...\n{'=-'*20}\n")
        if True:
            system("cls")
            return Jogo_Par_Impar()
    elif vlr == "I" and total % 2 != 0:
        input(f"VOCÊ VENCEU!\nVamos jogar novamente...\n{'=-'*20}\n")
        if True:
            system("cls")
            return Jogo_Par_Impar()
    elif vlr == "I" and total % 2 == 0:
        input(f"VOCÊ PERDEU!\nVamos jogar novamente...\n{'=-'*20}\n")
        if True:
            system("cls")
            return Jogo_Par_Impar()

Jogo_Par_Impar()