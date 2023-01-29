#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por Km rodado.

percurso_km = float(input("Quantos quilômetros foram rodados pelo carro alugado?:Km"))
dias = float(input("Por quantos dias foi usado o carro?:"))

preço = (dias*60.00)+0.15*percurso_km

print(f"O preço é de {preço}")
