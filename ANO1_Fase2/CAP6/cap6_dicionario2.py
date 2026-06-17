dicionario = {"Yoda":"Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "Ahsoka":"Padawan", "C3PO":"Droid",}
print(dicionario)

novo_jedi = input("Informe o nome do Jedi: ")
nova_cat_jedi = input("Informa a categoria do Jedi: ")

# IMPORTANTE: NÃO PERMITE REPETIÇÃO NA CHAVE, não adiciona outro "Yoda", MAS PODE ALTERAR A CATEGORIA(VALOR)

# SE ESSA NOVA CHAVE NÃO EXISTE, O PYTHON INSERE ELA E O VALOR ARMAZENADO NELA
dicionario[novo_jedi] = nova_cat_jedi
print(dicionario)

dicionario.update({"Yoda": "Grão-Mestre Jedi"})

# REMOVENDO ITEM
dicionario.pop("Ahsoka")

# REMOVENDO ÚLTIMO ITEM, EM VERSÕES ANTIGAS REMOVE UM ALEATÓRIO
dicionario.popitem()

# REMOVENDO TODOS ITENS
dicionario.clear()


print(dicionario)