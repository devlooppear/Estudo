from random import randint
from time import sleep

comp = randint(0, 5)

print(f"""{'-=-'*15}
Estou pensando em um número, entre 0 e 5.
Em qual número estou pensando?
{'-=-'*15}""")

r = str(input())

print("PROCESSANDO.....")
sleep(3)

print(f"Pensei no número {comp}")

if comp == r:
    print("Você ganhou")
else:
    print("Você perdeu")