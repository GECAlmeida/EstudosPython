hug = 0
zez = 0
lui = 0

print("Digite o voto ou 0 para finalizar")
print("1 - Huguinho")
print("2 - Zezinho")
print("3 - Luizinho")
print("0 - Terminar a votação")


while True:
    voto = int(input("Digite o voto: "))

    if voto == 1:
        hug = hug + 1
    elif voto == 2:
        zez = zez + 1
    elif voto == 3:
        lui = lui + 1
    else:
        if voto != 0:
            print("Voto inválido, digite: 1, 2, 3 ou 0 para finalizar")

        if voto == 0:
            break

print(f"Huguinho: {hug}", " votos")
print(f"Zezinho: {zez}", " votos")
print(f"Luizinho: {lui}", " votos")