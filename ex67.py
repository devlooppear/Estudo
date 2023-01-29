num = 0

while num >= 0:
    print(F"{'-'*35}\n Quer ver a tabuada de qual valor?:\n{'-'*35}")
    num = int(input())
    if num >= 0:
        for i in range(1, 11, 1):
            print(f" {num} X {i} = {num*i}")
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")