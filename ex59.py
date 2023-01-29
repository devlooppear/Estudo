import os
opcao = -1

def Menu():
    p1 = int(input("Primeiro Valor:"))
    p2 = int(input("Segundo Valor:"))
    print(f"""O que você quer fazer com esses valores?
    {'-='*10}
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Números
    [5] - Sair do Programa
    {'-='*10}""")

    opcao = int(input("Qual opção?:"))
    return opcao, p1, p2
def Soma(p1,p2):
    soma = p1 + p2
    print(f"A soma entre {p1} e {p2} é {soma}")
def Mult(p1,p2):
        mult = p1 * p2
        print(f"A multiplicação entre {p1} e {p2} é {mult}")
def Maior(p1,p2):
    maior = -1
    if p1 > p2:
        maior = p1
    else:
        maior = p2
        print(f"O maior número entre {p1} e {p2} é {maior}")
def Voltar():
    vol = input("Pressione quelquer botão para voltar...")
    if vol == True:
        return

def main():

    while True:
        os.system("cls")
        opcao, p1, p2 = Menu()
        if opcao == 1:
            os.system("cls")
            Soma(p1,p2)
            Voltar()
            opcao = -1
        elif opcao == 2:
            os.system("cls")
            Mult(p1,p2)
            Voltar()
            opcao = -1
        elif opcao == 3:
            os.system("cls")
            Maior(p1,p2)
            Voltar()
            opcao = -1
        elif opcao == 4:
            os.system("cls")
            Menu()
        if opcao == 5:
            break

main()