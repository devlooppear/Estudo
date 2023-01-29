from random import choice
n1 = str(input("Digite o Primeiro aluno:"))
n2 = str(input("Digite o Segundo aluno:"))
n3 = str(input("Digite o Terceiro aluno:"))
lista = [n1, n2, n3]
escolhido = choice(lista)
print(f"O nome escolhido foi {escolhido}")