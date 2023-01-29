salario = float(input("Digite um salário para ser calculoado o aumento: R$"))
aumento = float(input("Quanto de aumento (em porcentagem) terá o salário?%"))
novo_salario = ((salario*aumento)/100)+salario
print(f"O novo salário será de: {novo_salario:.1f}")