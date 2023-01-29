r1 = float(input("Digite o Primeiro segmento:"))
r2 = float(input("Digite o Segundo:"))
r3 = float(input("Digite o Terceiro:"))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print("Esses segmentos PODEM formar um triângulo.")
    if r1 == r2 == r3:
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓCELES")
else:
    print("Esses segmentos NÃO PODEM formar um triângulo.")

