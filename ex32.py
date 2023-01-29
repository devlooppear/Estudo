n1 = float(input(f"Informe o Primeiro Valor:"))
n2 = float(input(f"Informe o Segundo Valor:"))
n3 = float(input(f"Informe o Terceiro Valor:"))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print(f"O menor valor é o {menor}")
print(f"O maior valor é o {maior}")