pessoas_ricas = """Elon Musk ($219B);
Jeff Bezos ($171B);
Bernard Arnault e família ($158B);
Bill Gates ($129B);
Warren Buffett ($118B);
Larry Page ($111B);
Sergey Brin ($107B);
Larry Ellison ($106B);
Steve Ballmer ($91,4B);
Mukesh Ambani ($90,7B)""".split(";")
consulta = 0
while consulta not in range (1,11,1):
    print(f"{'='*41}\n  TOP 10 PESSOAS MAIS RICAS  (JAN-2023)\n{'='*41}")

    consulta = int(input("Digite a posição desejada para saber (entre 1 e 10): "))
print(f"O mais rico na {consulta}º posição é o :{pessoas_ricas[consulta-1]}")