# AO INVÉS DE USAR ALGO ASSIM:...
#personagens = []
#categorias = []

#for x in range(3):
#    personagens.append(input("Informe o nome do personagem: "))
#    categorias.append(input("Informe a categoria do personagem: "))

#for indice in range(3):
#    print(f"O personagem {personagens[indice]} é um {categorias[indice]}")


# CRIAÇÃO DO DICIONARIO:
              #chave:valor                 chave:valor                  chave:valor
dicionario = {"Yoda":"Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "Ahsoka":"Padawan", "C3PO":"Droid",}
print(dicionario)

# PEGA O VALOR DA CHAVE
print(dicionario["Yoda"])
# OU
print(dicionario.get("Yoda"))

print("\nChave Dicionário")
for chave in dicionario.keys():
    print(chave)

print("\nValor Dicionário")
for valor in dicionario.values():
    print(valor)

print("\nItens Dicionário")
for chave, valor in dicionario.items():
    print(f"{chave}-{valor}")