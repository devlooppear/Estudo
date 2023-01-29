produtos = []
precos = []
cnt = ""
while cnt != "N":
    produto = str(input("Digite um produto: "))
    preco = float(input("Digite um preço:R$ "))
    cnt = str(input("Deseja continuar?[S/N]): ").upper().strip())
    produtos.append(produto)
    precos.append(preco)

print(f"{'-'*48}\n               LISTAGEM DE PREÇO       \n{'-'*48}")

for produto, preco in zip(produtos,precos):
    tratar = str(preco)
    pontos = 30-len(produto)
    espacos = 15-len(tratar.strip("."))
    print(f"{produto}{'.'*pontos}R${' '*espacos}{preco:.2f}")

print(f"{'-'*48}")