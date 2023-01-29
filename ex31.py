from datetime import date
ano = int(input("Que ano você quer analiser?\nColoque [0] caso queira analisar o ano atual:"))
if ano == 0:
    ano = date.today().year
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print(f"O ano {ano} é um ano BISSEXTO")
else:
    print(f"O ano {ano} NÃO é um ano BISSEXTO")