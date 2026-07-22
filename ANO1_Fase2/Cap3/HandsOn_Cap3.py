totalimpar = 0
totalpar = 0

for i in range(1, 51):
    nota = float(input(f"Nota aluno {i}: "))

    if nota < 0 or nota > 10:
        print("Nota inválida!")
        continue ##CUMPRE FUNÇÃO DO ELSE, vai pro próximo i

    if i % 2 == 0:
        totalpar += nota
    else:
        totalimpar += nota

mediaimpar = totalimpar / 25
mediapar = totalpar / 25

if mediaimpar > mediapar:
    print("Ímpar ganhou, com média:", mediaimpar)
elif mediaimpar < mediapar:
    print("Par ganhou, com média:", mediapar)
else:
    print("Empate")