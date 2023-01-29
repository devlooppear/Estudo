#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250, calcule um aumento de 10% e para salários inferiores, um aumento de 15%

sal = float(input("Digite qual o salário:"))

if sal > 1250:
    nv_sal = (sal*(10/100))+sal
else:
    nv_sal = (sal*(15/100))+sal

print(f"Seu novo salário é de {nv_sal:.2f}")