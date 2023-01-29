saque = 0
cinquenta = 0
dez = 0
cinco = 0
um = 0

print(f"{'='*30}\n         BANCO PVP  \n{'='*30}")
saque = int(input("Que valor você quer sacar?: "))
if saque >= 50:
    cinquenta = saque / 50
    cinquenta = int(cinquenta)
    saque = saque % 50
    print(saque)
if saque < 50 and saque >= 10:
    dez = saque / 10
    dez = int(dez)
    saque = saque % 10
    print(saque)
if saque < 10 and saque >= 0:
    cinco = saque / 5
    cinco = int(cinco)
    saque = saque % 5
elif saque < 5 and saque >= 0:
    um = int(um)
    um = saque
print(f"""Total de {cinquenta} cédulas de R$50
Total de {dez} cédulas de R$10
Total de {cinco} cédulas de R$5
Total de {saque} cédulas de R$1
{'='*30}
Volte sempre ao BANCO PVP! Tenha um bom dia!
""")
