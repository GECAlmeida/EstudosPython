totalimpar = 0
totalpar = 0

for i in range(1, 11):

    # loop para garantir nota válida
    while True:
        nota = float(input(f"Nota aluno {i}: "))

        if 0 <= nota <= 10:
            break  # sai do while, nota válida
        else:
            print("Nota inválida! Digite novamente.")

    # agora estamos 100% seguros que nota é válida
    if i % 2 == 0:
        totalpar += nota
    else:
        totalimpar += nota

# como agora SEMPRE teremos 25 ímpares e 25 pares válidos
mediaimpar = totalimpar / 25
mediapar = totalpar / 25

if mediaimpar > mediapar:
    print("Ímpar ganhou, com média:", mediaimpar)
elif mediaimpar < mediapar:
    print("Par ganhou, com média:", mediapar)
else:
    print("Empate")