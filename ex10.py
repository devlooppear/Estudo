print("""Calculo para área de uma parede e quanto de tinta seria necessário,
 tendo que a cada 2 metros quadrados de área, se usa 1 litro de tinta""")
largura = float(input("Digite a Largura da parede (em metros):"))
altura = float(input("Digite a Altura da parede (em metros):"))
area = largura*altura
tinta = area/2
print(f"""
Para a largura {largura} e a altura {altura},
Sua área é de {area:.1f}.
Serão necessários {tinta:.1f}L de tinta
""")