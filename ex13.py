temperatura = float(input("""Escreva uma temperatura, em Celsius
para ser convertida para Fahrenheit e Kelvin: Cº"""))
f = ((temperatura*9)+32)/5
k = temperatura+273

print(f"{temperatura} Celsius, são {f} Fahrenheit e {k} Kelvin")