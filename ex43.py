val = float(input("Preço da compra:R$"))
print(f"|{'-='*5}LOJA=LOJAS{'-='*5}|")
print("""FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x no cartão ou mais
Escolha uma opção:
""")
opcao = -1
opcao = int(input(""))

if opcao == 1:
    preco = val-(val*0.10)
elif opcao == 2:
    preco = val-(val*0.05)
elif opcao == 3:
    preco = val
    print(f"Sua compra será parceladas em 2x de R${preco/2:.2f} por parcela")
elif opcao == 4:
    par = int(input("Quantas parcelas?:"))
    preco = val*1.20
    print(f"Sua compra será parceladas em {par}x de R${preco/par:.2f} por parcela\nCOM JUROS")
print(f"Sua compra de R${val:.2f} vai custar vai custar R${preco:.2f} no final.")