# LER O VALOR E PORCENTAGEM
valor = input("Digite o valor: R$")
porc  = input("Digite a porcentagem: ")

valor = float(valor)
porc = float(porc)

# CALCULAR PERCENTUAL, ACRESCIMO, DESCONTO E PERCENTUAL
perc = valor * porc / 100
acresc = valor + perc
desc = valor - perc

# EXIBIR RESULTADO
print("Percentual: ",perc)
print("Acréscimo: ", acresc)
print("Desconto: ",desc)