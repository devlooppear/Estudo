def cidade():
    cidade = ""
    while cidade[:5] != "Santo".upper():
        cidade = str(input("Qual cidade você nasceu?:").upper()).strip()
        if cidade[:5] == "Santo".upper():
            print(True)
            break

        elif cidade[:5] != "Santo".upper():
            print(False)

        else:
            print("Valor inválido")
cidade()