#Conferir se é possível formar um triângulo com determinados lados
n1 = float(input("Digite o Primeiro lado:"))
n2 = float(input("Digite o Segundo lado:"))
n3 = float(input("Digite o Terceiro lado:"))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Os segmentos acima PODEM FORMAR UM TRIÂNGULO")
else:
    print("Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO")