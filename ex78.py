numeros = []
cont = 0
maior = 0
menor = 0

for i in range(0, 5, 1):
    num = int(input(f"Digite um valor na posição {i}: "))
    numeros.append(num)
    cont = cont + 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
print('=-'*30)
print("Você digitou os valores:", end=" ")
for n in numeros:
    print(n, end=" ")
print(f"\nO maior valor digitado foi {maior} nas posições:", end=" ")

for i, n in enumerate(numeros):
    if n == maior:
        print(i, end="... ")

print(f"\nO menor valor digitado foi {menor} nas posições:", end=" ")

for i, n in enumerate(numeros):
    if n == menor:
        print(i, end="... ")