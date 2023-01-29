n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

m = (n1+n2)/2
print(f"Com a nota  de {n1} e {n2}, sua nota é de: {m}")

if m >= 5:
    print("APROVADO!")
else:
    print("REPROVADO!")