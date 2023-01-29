cont = """zero um dois três quatro cinco seis sete oito nove dez onze doze treze
quatorze quinze dezesseis dezessete dezoito dezenove vinte""".split()
num = -1
while num not in range(0, 21, 1):
    num = int(input("Digite um número entre 0 e 20: "))
    if num in range(0, 21, 1):
        break
    else:
        print("Tente novamente")
        num = int(input("Digite um número entre 0 e 20: "))

print(f"Você digitou o número {cont[num]}")