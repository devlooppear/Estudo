cnt = ""
total = 0
count_mai_mil = 0
maior = 0
menor = 0
count = 0
while cnt != "N":
    print(f"{'-'*30}\n      LOJA INOVA AGORA \n{'-'*30}")
    nome_p = str(input("Nome do Produto: "))
    preco = float(input("Preço: R$"))
    cnt = str(input("Quer continuar?[S/N]:").upper().strip())
    total = total + preco
    count = count + 1
    if preco > 1000:
        count_mai_mil = count_mai_mil + 1
    if count == 1:
        maior = preco
        menor = preco
    else:
        if preco > maior:
            maior = preco
        if preco < menor:
            nome_p = nome_p
            menor = preco
print(f"""{'-'*15} FIM DO PROGRAMA {'-'*15}\n
O total da compra foi R${total:.2f}
Temos {count_mai_mil} produtos custando mais que R$1000.00
O produto mais barato foi {nome_p} que custa {menor:.2f}
""")    
