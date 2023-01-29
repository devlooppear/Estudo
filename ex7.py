medida = float(input("Digite um valor em metros para ser convertido: "))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000
print(f"""{medida} em metros são:

{km} quilômetros
{hm} hectômetros
{dam} decâmetros
{dm:.0f} decímetros
{cm:.0f} centímetros
{mm:.0f} milímetros

""")