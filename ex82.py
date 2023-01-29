cnt = "S"
numeros = []
while cnt != "N" and cnt == "S":
    num = int(input("Digite um número: "))
    cnt = str(input("Deseja continuar?[S/N]: ").strip().upper())
    numeros.append(num)

print("A lista completa é:", end=" ")
for n in numeros:
    print(n, end=" ")
print("\nA lista de pares é:", end=" ")
for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")
print("\nA lista de ímpares é:", end=" ")
for n in numeros:
    if n % 2 != 0:
        print(n, end=" ")