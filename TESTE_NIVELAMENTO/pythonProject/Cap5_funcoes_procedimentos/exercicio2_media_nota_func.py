# FUNCAO BOOLEANA QUE VERIFICA SE UMA NOTA É VALIDA OU NAO
def nota_valida(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False

# FUNCAO QUE RETORNA O MENOR ENTRE 3 VALORES
def menor3n(n1, n2, n3):
    menor = n1
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

# FUNCAO QUE CALCULA A MEDIA DAS 2 MAIORES NOTAS
def media2maiores(n1, n2, n3):
    menor = menor3n(n1, n2, n3)
    return (n1 + n2 + n3 - menor) / 2

# PROCEDIMENTO PARA EXIBIR A MEDIA SEMESTRAL
def msg_media_semestral(m):
    print(f"A sua média semestral é {m:.1f}")

# FUNCAO QUE CALCULA A MEDIA DE 2 NUMEROS
def media2n(n1, n2):
    return (n1 + n2) / 2

# FUNCAO QUE RETORNA UMA MSG DE APROVADO OU NAO NO EXAME
def msg_aprovado_exame(m):
    if  m < 5:
        return f"Reprovado em exame com média {m:.1f}"
    else:
        return f"Aprovado em exame com média {m:.1f}"


nota1 = float(input("Nota 1: "))

if nota_valida(nota1):
    nota2 = float(input("Nota 2: "))

    if nota_valida(nota2):
        nota3 = float(input("Nota 3: "))

        if nota_valida(nota3):

            media_semestral = media2maiores(nota1, nota2, nota3)
            msg_media_semestral(media_semestral)

            if media_semestral < 4:
                print("Você está reprovado direto")
            elif media_semestral >= 7:
                print("Você está aprovado direto")
            else:
                print("Você ficou em exame")

                nota_exame = float(input("Digite a nota do exame: "))

                if nota_valida(nota_exame):
                    media_exame = media2n(media_semestral, nota_exame)

                    print(msg_aprovado_exame(media_exame))
                else:
                    print(f"Nota de exame {nota_exame} inválida!")

        else:
            print(f"Nota 3: {nota3} é inválida!")

    else:
        print(f"Nota 2: {nota2} é inválida!")

else:
    print(f"Nota 1: {nota1} é inválida!")