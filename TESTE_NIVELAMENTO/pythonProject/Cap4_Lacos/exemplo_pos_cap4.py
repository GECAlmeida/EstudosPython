soma = 0

# NÃO EXISTE 'DO' NO PYTHON, TRUE FAZ WHILE JÁ COMEÇAR SEM PRE-CONDICIONAL
while True:
    num = float(input("Digite um número: "))
    if num >= 0: # 'IF' FUNCIONA COMO O WHILE DO JAVA NO POS-CONDICIONAL
        soma = soma + num
    else:
        break # BREAK INTERROMPE SE NÃO FOR MAIOR OU IGUAL A 0

print("Soma: ", soma)
