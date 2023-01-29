num = -1
con = ""
count = 0
soma = 0
maior = 0
menor = 0
while con != "N":
    num = int(input("Digite um número: "))
    con = str(input("Quer continuar?: ").upper())
    count =  count + 1
    soma = soma + num
    if count == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma/count
print(f"Você digitou {count} números e sua média é {media:.2f}")
print(f"O maior valor foi o {maior} e o menor valor foi o {menor}")