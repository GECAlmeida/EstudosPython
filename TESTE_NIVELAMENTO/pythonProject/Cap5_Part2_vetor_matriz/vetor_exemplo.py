vetor = [];

# 1 - PREENCHER O VETOR
for i in range(0, 10, 1):
    print(f"Digite a posição: vetor[{i}]= ")
    elem = int(input())
    vetor.append(elem)

# 2 - EXIBIR O CONTEÚDO DO VETOR
for i in range(0, 10, 1):
    print(f"vetor[{i}]= {vetor[i]}")

# 3 - SOMAR OS ELEMENTOS DO VETOR
soma = 0
for i in range(0, 10, 1):
    soma += vetor[i];

print (f"Somatória do vetor = {soma}")

# 4 - BUSCAR UM ELEMENTO NO VETOR
achou = False

# Digitação do elemento que será procurado
elem = int(input("Digite o elemento:"))
for i in range(0, 10, 1):
    # Caso encontre o elemento, interrompe a busca
    if vetor[i] == elem:
        achou = True
        break

# Analisa se encontrou ou não o elemento
if (achou):
    print(f"Elemento {elem} encontrado no vetor")
else:
    print(f"Elemento {elem} NÃO  foi encontrado no vetor")