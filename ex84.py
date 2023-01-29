cnt = "S"
count = 0
maior = 0
menor = 0
nomes_maior = []
nomes_menor = []
while cnt == "S" and cnt != "N":
    count = count + 1
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    cnt = str(input("Deseja Continuar?[S/N]: ").upper().strip())

    if count == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso
    if maior == peso:
        nomes_maior.append(nome)
    elif menor == peso:
        nomes_menor.append(nome)

     
print(f"{30*'=-'}")

print(f"Os maiores pesos foram de {maior:.1f}Kg, Peso de {nomes_maior}")
print(f"Os menores pesos foram de {menor:.1f}Kg, Peso de {nomes_menor}")