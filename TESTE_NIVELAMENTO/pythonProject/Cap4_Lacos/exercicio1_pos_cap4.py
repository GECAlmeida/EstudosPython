soma = 0

while True:
    num = float(input("Digite um número maior que 10: "))
    if num < 0:
        break

    if num > 10:
        soma = soma + num

print("Soma: ", soma)

