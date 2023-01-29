num = int(input("Digite um número:"))
razao = int(input("Digite sua razão:"))
print(f"A PA de {num} com uma razao de {razao} é:")
print(f"{'-='*15}")
for i in range(0,10*razao,razao):
    pa = num+i
    print( pa, end=" -> ",)
print("FIM")
print(f"{'-='*15}")