num = int(input("Digite um número para saber seus divisores:"))
tot = 0
for i in range(1, num+1, 1):
    if num % i == 0:
        tot = tot+1
        print("\33[32m", end=" ")
    else:
        print("\33[31m", end=" ")
    print(f"{i}", end=" ")
if tot == 2:
    print("\n\033[mEsse número é primo")
else:
    print("\n\033[mEsse número não é primo")