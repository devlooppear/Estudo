from datetime import date
atual = date.today().year
som_ma = 0
som_me = 0
for pess in range(1, 8, 1):
    nasc = int(input(f"Em que ano a {pess} pessoa nasceu?: "))
    idade = atual - nasc
    if idade >= 18:
        print("Essa pessoa é maior")
        som_ma = som_ma+1
    else:
        print("Essa pessoa é menor")
        som_me = som_me+1
print(f"Temos {som_ma} pessoas maiores de idade e")
print(f"temos {som_me} pessoas menores de idade")