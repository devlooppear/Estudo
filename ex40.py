from datetime import date

ads = int(input("Digite seu ano de nascimento:"))
ida = date.today().year-ads
print(f"Quem nasceu em {ads} tem {ida} anos")
print("Classificação:")
if ida <= 9:
    print("MIRIM")
elif ida > 9 and ida <= 14:
    print("INFANTIL")
elif ida > 14 and ida <= 19:
    print("JUNIOR")
elif ida > 19 and ida <= 25:
    print("SÊNIOR")
elif ida > 25:
    print("MASTER")
else:
    print("Valor inválido")