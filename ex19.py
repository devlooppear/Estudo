from random import shuffle

n1 = str(input("Digite o Primeiro nome:"))
n2 = str(input("Digite o Segundo nome:"))
n3 = str(input("Digite o Terceiro nome:"))

lista = [n1,n2,n3]
shuffle(lista)
print(f"A nova ordem de nomes é: {lista}")