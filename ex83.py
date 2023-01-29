expr = str(input("Digite a expressão: ").strip().split())
print(expr)
simbolo_1 = []
simbolo_2 = []
if expr == "(":
    simbolo_1.append(expr)
if len(simbolo_1) <= len(simbolo_2):
    if expr == ")":
        simbolo_2.append(expr)
if len(simbolo_1) == len(simbolo_2):
    print("Expressão válida!")
else:
    print("Expressão inválida!")