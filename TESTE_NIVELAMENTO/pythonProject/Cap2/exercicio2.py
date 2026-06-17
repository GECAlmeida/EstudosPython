
prec_maco = float(input("Digite o preço do maço: "))

qtd_maco = float(input("Digite a qtd de maços: "))

anos = float(input("Digite a qtd de anos que fuma: "))

dias_fumante = anos * 365

custo = prec_maco * qtd_maco * dias_fumante

print("Você já gastou R$ ", custo, " Fumando")
