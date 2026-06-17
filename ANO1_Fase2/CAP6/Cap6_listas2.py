jedi = ["Anakin", "Luke", "Yoda", "Obi-Wan"]
outros_jedi = ["Qui-Gon-Jinn", "Mace Windu", "Kit Fisto", "Dooku"]
# FUNDINDO LISTAS PARA CRIAR UMA NOVA
todos_jedi = jedi + outros_jedi
print(todos_jedi)

# ADICIONANDO UMA LISTA A OUTRA
jedi.extend(outros_jedi)
print("Jedi alterado")
print(jedi)

# CRIAR UMA LISTA CÓPIA DE OUTRA
jedi_copia = jedi.copy()
jedi_copia.append("Rey")
print(jedi_copia)

# TAMANHO DA LISTA
print(f"\nTamanho da lista: {len(jedi)}")
# METODO PARA CONTAR QUANTAS VEZES APARECE
print(f"O valor de Yoda aparece na lista: {jedi.count("Yoda")} vez")

# REVERTE LISTA
jedi.reverse()
print(jedi)

# ORDENAR LISTA, ORDEM ALFABETICA, ***ISSO ALTERA A LISTA***
jedi.sort()
print(f"Ordenando a lista: {jedi}")