# LAÇO PRÉ-CONDICIONAL (0, N)

opcao = input("Digite [S]im ou [N]ão: ")
while opcao != "s" and opcao != "S" and opcao != "n" and opcao != "N":
    print("Você digitou ", opcao, ", digite S ou N!")
    opcao = input("Digite [S]im ou [N]ão: ")

print("Você digitou ", opcao)