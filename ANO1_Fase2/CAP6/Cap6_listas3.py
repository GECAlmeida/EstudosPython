valores = [2, 3, 5, 10]
print(valores)

# SOMAR ELEMENTOS
soma = sum(valores)
print("A soma dos elementos é: {:.2f}".format(soma))

# EXEMPLO DE SLICE - LIST SLICING

#         0         1        2        3            4              5             6          7
jedi = ['Anakin', 'Luke', 'Yoda', 'Obi-Wan', 'Qui-Gon-Jinn', 'Mace Windu', 'Kit Fisto', 'Dooku']
#         -8       -7        -6      -5           -4            -3             -2         -1
                            # INICIO:FIM(PAROU DE INCLUIR APÓS O 2)
print(f"Os primeiros 3 jedis: {jedi[0:3]}") # OU [:3]
print(f"Os últimos 3 jedis: {jedi[-3:]}")
print(f"Do segundo ao penúltimo: {jedi[1:-1]}")

# LIST SLICING - [INICIO:FIM:PASSO]-
print(f"Somente os pares: {jedi[::2]}") # A CADA 2 PASSOS - 0, 2, 4...
# IMPRIMIR LISTA INVERTIDA
print(f"Invertendo a lista: {jedi[::-1]}") # PASSO NEGATIVO

# DELETANDO ELEMENTO DA LISTA
del jedi[-1]
print(jedi)

# INVERTENDO STRING
nome = "Anakin"
print(nome[::-1])

#IMPRIMINDO ELEMENTO INVERTIDO
print(jedi[4][::-1])