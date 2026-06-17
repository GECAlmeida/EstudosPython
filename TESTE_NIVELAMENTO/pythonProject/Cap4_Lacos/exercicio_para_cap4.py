soma = 0
num = float(input("Digite 10 números: "))

for cont in range(1, 10, 1):
    num = float(input())
    soma = soma + num

print("Soma: ", soma)