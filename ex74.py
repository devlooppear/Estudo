from random import randint
count = 0
numeros = []
maior = 0
menor = 0
for i in range(1,6,1):
    i = randint(1,10)
    numeros.append(i)
print(f"Os valores sorteados foram:")
for n in numeros:
    print(f"{n}", end=" ")
    count = count + 1
    if count == 1:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
print(f"\nO maior número foi: {maior}")
print(f"O menor número foi: {menor}")