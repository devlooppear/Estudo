num = -1
soma = 0
count = 0
while num != 999:
    num = int(input("Digite um valor (999 para parar): "))
    soma = soma + num
    count = count + 1
soma = soma - 999
print(f"A soma dos {count} valores é {soma}")