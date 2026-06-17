valor = int(input("Digite o valor: "))

ced50 = valor // 50
valor = valor % 50
ced20 = valor // 20
valor = valor % 20
ced10 = valor // 10
valor = valor % 10

print("Quantidade de cédulas de 50: ", ced50)
print("Quantidade de cédulas de 20: ", ced20)
print("Quantidade de cédulas de 10: ", ced10)
