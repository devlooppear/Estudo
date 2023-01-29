print("-="*10)
print("Gerador de PA")
print("-="*10)
primeiro = int(input("Primeiro Termo:"))
razao = int(input("Razão da PA:"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} ->", end= " ")
        termo = termo + razao
        cont = cont + 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progeressão finalizada com {total} termos")