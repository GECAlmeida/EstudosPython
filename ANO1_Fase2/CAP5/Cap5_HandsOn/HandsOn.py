def calcula_pizza(tamanho, qtd_sabores):
    if tamanho.lower() == "pequena":
        preco = 20
    elif tamanho.lower() == "media":
        preco = 30
    else:
        preco = 40
    preco += (qtd_sabores - 1) * 5
    return preco

tamanho_pizza = input("Escolha o tamanho: ")
sabores = int(input("Quantidade de sabores: "))

print(calcula_pizza(tamanho_pizza, sabores))