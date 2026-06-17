#soma = lambda a, b: a+b
#print("Soma: ", soma(1,2))

verifica_positivo = lambda x: "Positivo" if x >=0 else "Negativo"
print(verifica_positivo(-10))

# SEM PRECISAR NOMEAR LAMBDA, MELHOR
# print(list(map(lambda x: "Positivo" if x >= 0 else "Negativo", [-5, 2, 0])))

# LAMBDA COMO ARGUMENTO DE OUTRA FUNÇÃO, FUNC É VARIÁVEL
# func = lambda f: f(int(input("Digite um número: ")))
# print(func(lambda x: "Positivo" if x >= 0 else "Negativo"))