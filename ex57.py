sexo = ""
while sexo.upper() not in ["M","F"]:
    sexo = str(input("Informe seu sexo(M/F):").upper())
    if sexo.upper() in ["M","F"]:
        break