n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

operador = str(input("Digite a operação desejada (+ - * /): "))

if operador == '+':
    res = n1 + n2
    print("Soma = ", res)
elif operador == '-':
    res = n1 - n2
    print("Subtração = ", res)
elif operador == '*':
    res = n1 * n2
    print("Multiplicação = ", res)
elif operador == '/':
    if n2 == 0:
        print("Não existe divisão por zero")
    else:
        res = n1 / n2
        print("Divisão = ", res)
else:
    print("Operador inválido! ")