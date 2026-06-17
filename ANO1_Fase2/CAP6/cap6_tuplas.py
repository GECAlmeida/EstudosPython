categorias = ("Youngling", "Padawan", "Knight", "Master")
print(categorias)

categorias = tuple(("Youngling", "Padawan", "Knight", "Master"))
print(categorias)
print(categorias[-1])

for categoria in categorias:
    print(categoria)

# COLOCAR UMA VIRGULA PARA A CLASSE SER CONSIDERADA UMA TUPLA, SE HOUVER APENAS UM ELEMENTO
categorias = ("Padawan",)
print("\n",categorias)
print(type(categorias))

categorias = ("Padawan") # SEM VIRGULA, VIRA STR
print("\n",categorias)
print(type(categorias))

categorias = ("Youngling", "Padawan", "Knight", "Master")
print(f"Tamanho da tupla {len(categorias)}")

# TUPLAS SÃO IMUTÁVEIS, NÃO DÁ PRA FAZER DEL OU APPEND

categorias_sith = ("Acolyte", "Sith-Lord")
categorias_jedi = ("Youngling", "Padawan", "Knight", "Master")
categorias = categorias_jedi + categorias_sith
print("\n", categorias)

posicao = categorias.index("Padawan")
print(posicao)

if "Knight" in categorias:
    print("Knight está presente na tupla")


# CONVERTENDO LISTA EM TUPLA
lista = [1, 2, 3]
t = tuple(lista)
print("\n", t)

# OU
t = tuple("Python")
print("\n",t)