ini = int(input("Digite o numero inicial: "))
fin = int(input("Digite o numero final: "))

while True:
    print(ini)
    ini += 1
    if ini > fin:
        break

# SEM EXIBIR INICIAL E FINAL
ini = int(input("Digite o numero inicial: "))
fin = int(input("Digite o numero final: "))

while True:
    ini += 1

    if ini >= fin:
        break

    print(ini)