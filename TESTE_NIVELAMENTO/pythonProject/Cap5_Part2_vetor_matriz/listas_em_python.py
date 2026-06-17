"""
LISTAS EM PYTHON

- O CONTEUDO DOS ELEMENTOS É HETEROGENEO
- ELEMENTOS SAO DINAMICOS, ACRESC E EXCL QUANDO QUISER
- O append ACRESC UM ITEM NO FINAL.                         lista.append(45)
- O INSERT PERMITE EDITAR ELEMENTO.                         lista.insert(indice, conteudo)
- O POP REMOVE O ULTIMO ELEMENTO DA LISTA.                  lista.pop()
- O CLEAR APAGA TODOS ELEMENTOS.                            lista.clear
"""

# elementos heterogêneos na lista:
# indices: 0   1   2   3
lista = ["a", 2, True, 4.5] # tipos: string, int, boolean e float
print(lista)

# adicionando no final da lista
lista.append(45)
print(lista)

# editando elemento existente (indice, elemento a ser inserido)
lista.insert(0, "FIAP")
print(lista)

# pop remove o ultimo elemento() ou qual escolher (1)
lista.pop()
print(lista)

# apaga todos elementos
lista.clear()
print(lista)