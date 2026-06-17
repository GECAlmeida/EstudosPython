# NOTA SERÁ O PARAMETRO QUE RECEBERÁ NOTA1 E NOTA2
def nota_valida(nota):
    if nota >= 0 and nota <= 10:

        # TRUE OU FALSE CONFIRMA OU NÃO
        return True
    else:
        return False

# OUTRA FORMA DE FAZER O MESMO SEM PRECISAR DO IF:

# def nota_valida(nota)
    # return 0 <= nota <= 10

nota1 = float(input("Digite a primeira nota: "))
# SE NOTA1 CORRESPONDE A NOTA (SUA FUNÇÃO)
if nota_valida(nota1):
    nota2 = float(input("Digite a segunda nota: "))
    if nota_valida(nota2):
        media = (nota1 + nota2) / 2
        print(f"A média das notas {nota1} e {nota2} é igual a {media}")
    else:
        print(f"A segunda nota: {nota2} é inválida!")
else:
    print(f"A primeira nota: {nota1} é inválida!")