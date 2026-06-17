print("Digite 0 para finalizar")
# Essa variável irá acumular a soma, zerada para começar, devendo estar declarada para poder somar
soma = 0
# Deve começar diferente de zero para entrar no laço
num = 1

while num != 0:
    num = float(input("Digite um número: "))
    soma = soma + num

print("Somatória: ", soma)