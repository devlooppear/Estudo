peso = float(input("Qual seu peso?:(Kg)"))
alt = float(input("Qual sua altura?:(m)"))

imc = peso/(alt**2)
print(f"Seu Índice de Massa Corporal (IMC) é de:{imc:.2f}")
if imc < 18.5:
    print("BAIXO PESO")
elif imc > 18.5 and imc <= 24.9:
    print("PESO NORMAL")
elif imc > 24.9 and imc <= 29.9:
    print("EXCESSO DE PESO")
elif imc > 29.9 and imc <= 35.0:
    print("OBESIDADE")
elif imc > 35:
    print("OBESIDADE EXTREMA")
else:
    print("Valor Inválido!")