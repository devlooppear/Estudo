cnt = "S"
numeros = []
while cnt == "S" and  cnt != "N":
    num = int(input("Digite um número: "))
    cnt = str(input("Deseja continuar?: ").upper().strip())
    numeros.append(num)

print("Para os numeros:", end=" ")
for n in numeros:
    print(n, end=" ")
print("Os números pares são:")
for n in numeros:
    if n % 2 == 0 and n != 0:
        print(n, end=" ")
print("Os números ímpares são:")
for n in numeros:
    if n % 2 != 0 and n != 0:
        print(n, end=" ")