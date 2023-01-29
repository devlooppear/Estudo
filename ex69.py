cnt = ""
count_mai_ida = 0
count_hom = 0
count_mlr = 0
while cnt != "N":
    print(f"{'-'*30}\n    CADASTRAR UMA PESSOA  \n{'-'*30}")
    ida = int(input("Idade: "))
    sexo = str(input("Sexo[M/F]: ").upper())
    cnt = str(input(f"{'-'*30}\nQuer continuar?[S/N]: ").upper())
    if ida > 18:
        count_mai_ida = count_mai_ida + 1
    elif sexo == "M":
        count_hom = count_hom + 1
    elif sexo == "F" and ida <= 20:
        count_mlr = count_mlr + 1
    if cnt not in "SN".split() or sexo not in "MF".split():
        print("Caracter Inválido.")
print(f"""Total de pessoas com mais de 18 anos: {count_mai_ida}
Ao todo temos {count_hom} homens cadastrados
E temos {count_mlr} mulheres com menos de 20 anos
""")
