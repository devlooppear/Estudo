dis = float(input("Qual a distÂncia da sua viagem?:"))
if dis <= 200:
    pre = dis * 0.5
else:
    pre = dis * 0.45
print(f"P preço será de R${pre:.2f}")