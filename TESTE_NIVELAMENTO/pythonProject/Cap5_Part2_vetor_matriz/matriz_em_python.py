# MANIPULANDO MATRIZ
matriz  = [ [0,0], [0,0], [0,0], [0,0]] # matrizes funcionam como uma lista de listas [0,0] DUAS COLUNAS
#             1      2      3      4     - QUATRO LINHAS     -----> MATRIZ 4x2

# 1) PREENCHER A MATRIZ
print("Preenchendo a matriz...")
for l in range(4): # É O MESMO QUE for lin range(0, 4, 1) indices 0, 1, 2, 3 (4 é o numero de  voltas, mas  já conta a primeira,por tanto indice = 4 - 1)
    for c in range(2):
        matriz[l][c] = int(input(f"Matriz[{l}][{c}] = "))

# 2) EXIBIR A MATRIZ
print("\nExibindo a matriz...")
for l in range(4):
    for c in range(2):
        print(f"{matriz[l][c]}\t", end = "") # end - para cada coluna, ele não pula linha,já \t não deixa grudado
    print()

# 3) SOMAR OS ELEMENTOS  DA MATRIZ
soma = 0

for l in range(4):
    for c in range(2):
        soma += matriz[l][c]

print("\nSoma = ", soma)

# IMPORTANTE: NÃO É NECESSARIO ESSES ULTIMOS LOOPS, SERVEM SÓ PARA DIDATICA.


# FORMA MAIS EFICIENTE DE LOOPING:

# soma  = 0
# for linha in matriz:
    # for elem in linha:
        #  soma += elem