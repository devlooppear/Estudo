from random import randint
from time import sleep
itens = ("Pedra Papel Tesoura").split(" ")
print(f"""{'-='*7}JOKENPÔ{'-='*7}
Escolha uma opção:
[1] PEDRA
[2] PAPEL
[3] TESOURA
{'-='*18}
""")
usu = -1
usu = int(input(""))
com = randint(1,3)
print(f"{'-='*18}")
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!")
print(f"{'-='*18}")

if usu == 1:
    print(f"Você escolheu {itens[0]}")
    if com == 1:
        print(f"O computador também escolheu {itens[0]}.\nEMPATE!")
    elif com == 2:
        print(f"O computador escolheu {itens[1]}.\nVOCÊ PERDEU!")
    elif com == 3:
        print(f"O computador escolheu {itens[2]}.\nVOCÊ VENCEU!")

elif usu == 2:
    print(f"Você escolheu {itens[1]}")
    if com == 1:
        print(f"O computador escolheu {itens[0]}.\nVOCÊ VENCEU!")
    elif com == 2:
        print(f"O computador também escolheu {itens[1]}.\nEMPATE!")
    elif com == 3:
        print(f"O computador escolheu {itens[2]}.\nVOCÊ PERDEU!")

elif usu == 3:
    print(f"Você escolheu {itens[2]}")
    if com == 1:
        print(f"O computador escolheu {itens[0]}.\nVOCÊ PERDEU!")
    elif com == 2:
        print(f"O computador escolheu {itens[1]}.\nVOCÊ VENCEU!")
    elif com == 3:
        print(f"O computador também escolheu {itens[2]}.\nEMPATE!")

else:
    print("Valor Inválido!")