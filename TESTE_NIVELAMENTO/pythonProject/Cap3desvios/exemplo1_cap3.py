venda = float(input("Digite o valor da venda: "))

if venda > 300:
    desc = venda * 10 / 100
    venda = venda - desc

print("O valor final é: ", venda)
