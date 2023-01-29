maior = 0
menor = 0
for i in range(1,6,1):
    pessoa = float(input(f"Quantos quilos tem a {i}º pessoa:"))
    if i == 1:
        maior = pessoa
        menor = pessoa
    else:
        if pessoa > maior:
            maior = pessoa
        if pessoa < menor:
            menor = pessoa
    
print(f"O maior peso lido foi:{maior}")
print(f"O menor peso lido foi:{menor}")