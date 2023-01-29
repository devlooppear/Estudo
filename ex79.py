cnt = "S"
numeros = []
count = 0
while cnt != "N" and cnt == "S":
    num = int(input("Digite um valor: "))
    if num not in numeros:
        print("Valor adicionado com sucesso...")
        numeros.append(num)
    else:
        print("Valor duplicado! Não será adicionado.")
    cnt = str(input("Quer continuar?: ").strip().upper())
print(numeros)