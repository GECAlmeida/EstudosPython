matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# 1 - PREENCHER A MATRIZ
for l in range(3):
    for c in range(4):
        matriz[l][c] = int(input(f"Matriz[{l}][{c}]= "))

# 2 - EXIBIR A MATRIZ
for l in range(3):
    for c in range(4):
        print(f"[{l}][{c}] = {matriz[l][c]}	")
    print()

# 3 - SOMAR OS ELEMENTOS DA MATRIZ
soma = 0
for l in range(3):
    for c in range(4):
        soma += matriz[l][c]

print("Soma = ", soma)

# 4 - BUSCAR UM ELEMENTO NO VETOR
achou = False
elem = int(input("Digite o elemento:"))
for l in range(3):
    for c in range(4):
        if matriz[l][c] == elem:
            achou = True
            break

if (achou):
    print(f"Elemento {elem} encontrado na matriz")
else:
    print(f"Elemento {elem} NÃO  foi encontrado na matriz")