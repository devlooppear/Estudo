vel = float(input("Qual a velocidade do carro?:"))

if vel < 80:
    print("Tenha um ótimo dia! Dirija com segurança.")
else:
    multa = (vel-80)*7
    print(f"""Epa! Aí não, meu patrão. Vou ter que te multar
sua multa é de R${multa:.2f}""")
