pares = []
numeros = []
count = 0

for i in range(1,5,1):
    n = int(input(f"Digite o {i}º:"))
    numeros.append(n)

print("Você digitou os números:", end=" ")
for n in numeros:
    print(n, end=" ")
    if n % 2 == 0:
        pares.append(n)

for i in range(1,4,1):
    if numeros[0] == numeros[i]:
        count = count + 1

print(f"\nO valor {numeros[0]} apareceu {count+1} vezes")
print(f"O valor {numeros[1]} apareceu na 2º posição")
print(f"Os valores pares digitados foram:", end= " ")
for n in pares:
    print(n, end=" ")