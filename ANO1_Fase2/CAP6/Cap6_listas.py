# PRIMEIRO JEITO DE FAZER LISTA
jedi = ["Anakin","Yoda","Luke","Obi-Wan"]
print(jedi)
# print(type(jedi))

# SEGUNDO JEITO DE FAZER LISTA - CONVERTENDO TUPLA PARA LISTA
# jedi2 = list(("Luke", "Qui-Gon-Jin", "Ahsoka"))
# print(type(jedi2))

# EQUIVALENCIA DO YODA
# print(jedi[1])
# ULTIMO INDICE É -1, VAI DIMINUINDO, UTIL QUANDO QUISER USAR O FINAL DA LISTA
# print(jedi[-2])

# nome É O ÍNDICE
for nome in jedi:
    print(nome)

# ADICIONA ELEMENTO AO FINAL DA LISTA
jedi.append("Mace Windu")
print(jedi)

# INSERIR ELEMENTO NOVO EM UM ÍNDICE EXISTENTE, O ELEMENTO ANTERIOR É MANDADO PARA O PRÓXMO ÍNDICE
jedi.insert(2, "Dooku")
print(jedi)

jedi.append(input("Entre com o novo jedi: "))
print(jedi)

# REMOVE ELEMENTO PELO ********INDICE**********
jedi.pop() # VAZIO REMOVE O ULTIMO
print(jedi)

# REMOVE PELO ***********ELEMENTO************ INSERIDO
jedi.remove("Yoda")
print(jedi)

jedi.pop(1) # REMOVE O INDICE 1
print(jedi)