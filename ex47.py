soma = 0
count = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        count = count+1
        soma = soma+i
print(f"A soma de todos os {count} valores dectados é:{soma}")