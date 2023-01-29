som = 0
cont = 0
for i in range(1,7):
    num = int(input(f"Digite o {i}º Valor:"))
    if num % 2 == 0:
        cont = cont+1
        som = som+num
print(f"Você digitou {cont} números pares e a soma deles foi: {som}")
