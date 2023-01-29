num = -1
count = 0
soma = 0
while num != 999:
    num = int(input("Digite um número [999 para parar]:"))
    soma = soma + num
    count = count+1
soma = soma - 999
count = count -1
print(f"Você digitou {count} números e a soma deles foi {soma}")