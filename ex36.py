num = int(input("Digite um número:"))
opcao = -1
opcao = int(input(f"""
Digite qual tipo de conversão você quer realizar:
{'-='*25}
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL
{'-='*25}
"""))
if opcao == 1:
    print(f"""Em BINÁRIO O número {num} fica da seguinte forma:
{bin(num)[2:]}""")
elif opcao == 2:
    print(f"""Em OCTAL O número {num} fica da seguinte forma:
{oct(num)[2:]}""")
elif opcao == 3:
    print(f"""Em HEXADECIMAL O número {num} fica da seguinte forma:
{hex(num)[2:]}""")
else:
    print("Opção Inválida!")