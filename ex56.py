mais_v = 0
mais_n = 0
som = 0
m_men_vint = 0
n_mais_v = ""
for i in range(1,5,1):
    print(f"{'-'*5}{i}ºPESSOA{'-'*5}")
    nome = str(input("Nome:"))
    ida = int(input("Idade:"))
    sexo = str(input("Sexo(M/F):"))
    som = som+ida
    if i == 1:
        mais_v = ida
        mais_n = ida
    else:
        if ida > mais_v:
            n_mais_v = nome
            mais_v = ida
        if ida < mais_n:
            mais_n = ida
    if ida < 20 and sexo == "F":
        m_men_vint = m_men_vint+1
media = som/4
print(f"A média da idade do grupo é {media} anos")
print(f"O homem mais velho é o {n_mais_v} e sua idade é {mais_v}")
print(f"Ao todo são {m_men_vint} mulheres, com menos de 20 anos")