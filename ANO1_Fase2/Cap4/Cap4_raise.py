# CÓDIGO A SER EXECUTADO
try:
    idade = int(input("Insira sua idade: "))

    if idade < 0:
        # RAISE GERA ARTIFICIALMENTE UMA EXCEÇÃO SE FOR MENOR QUE ZERO
        raise ValueError("Valor de idade não pode ser menor que zero!")

# EXCEÇÕES SENDO TRATADAS
except ValueError as error:
    print("Erro: ", error)
except Exception as error:
    print("Aconteceu um erro: ", error)
else:
    print(f"Você tem {idade} anos")