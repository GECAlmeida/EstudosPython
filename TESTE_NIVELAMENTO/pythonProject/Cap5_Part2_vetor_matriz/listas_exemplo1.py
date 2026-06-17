lista = []
# 1) preenchendo e exibindo lista
for cont in range(0, 5, 1):
    x = float(input("Digite um elemento: "))
    lista.append(x)
print(lista)

# 2) exibindo os 5 elementos da lista - FORMA 1
for i in range(0, 5, 1):
    print(lista[i]) # é como se tivesse feito: print(lista[0]), print(lista[1]), print(lista[2])...até 4, pois i=0, i=1, i=2...

# 2) FORMA 2
for elem in lista: # sem precisar de constantes, exibe quantos elementos estiverem na lista, como se a variavel elem se tornasse elemento de cada indice
    print(elem)

# 3) somando os elementos da lista
soma = 0
for elem in lista:
    soma += elem # o mesmo que soma = soma + elem.        +=(operador aritmetico de atribuição) <> = <> + <>(processo natural)
print("\nSoma = ", soma)
