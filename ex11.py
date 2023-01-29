import os

def calculo():
    print("Calculo para o valor de um produtor e seu desconto")
    valor = float(input("Qual o valor do produto?:R$"))
    desconto = float(input("Qual o desconto, em porcentagem, que você quer aplicar?:%"))
    valor_des = (valor*desconto)/100
    valor_final = valor-valor_des
    print(f"""
    Valor: {valor}
    Desconto: {desconto}%
    """)
    return valor,desconto,valor_des,valor_final

def confrimacao(valor,desconto,valor_des,valor_final):
    conferir = str(input("Os dados estão corretos (S/N)?: "))
    if conferir.upper() == "S":
        print(f"""Com o valor de R${valor} e o desconto de {desconto}%, o desconto é de: R${valor_des}
ficando então: R${valor_final}
        """)
    elif conferir.upper() == "N":
        input("Pressione qualquer tecla para voltar...")
        os.system("cls")
        return calculo()
    else:
        print("Caractere Inválido!")
        os.system("cls")
        return calculo()

def main():

    valor,desconto,valor_des,valor_final = calculo()

    confrimacao(valor,desconto,valor_des,valor_final)

main()