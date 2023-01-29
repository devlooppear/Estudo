"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor, o salário do comprador e em quantos anos ele vai pagar.
 A apresentação mensal não pode exceder 30% do salário ou então o empréstimo será negado"""

val = float(input("Digite o valor do imóvel:"))
sal = float(input("Digite o seu salário:"))
anos = int(input("Digite a quantidade de anos que pretende pagar:"))

tem_sal = (sal*(anos*12))

if val > tem_sal*0.30:
    print("VENDA NÃO APROVADA!")
    print(f"""Para pagar esta casa em {anos} anos,
 você teria o valor de R${tem_sal*0.30},
 considerando 30% do seu salário""")
else:
    print("COMPRA APROVADA!")
    print(f"""Para pagar esta casa em {anos} anos,
 você teria o valor de R${tem_sal*0.30},
 considerando 30% do seu salário""")