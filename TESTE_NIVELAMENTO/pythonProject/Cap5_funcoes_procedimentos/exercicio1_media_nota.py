nota1 = float(input("Digite a nota 1: "))
if nota1 < 0 or nota1 > 10:
    print("Nota inválida.")
else:
    nota2 = float(input("Digite a nota 2: "))
    if nota2 < 0 or nota2 > 10:
        print("Nota inválida.")
    else:
        nota3 = float(input("Digite a nota 3: "))
        if nota3 < 0 or nota3 > 10:
            print("Nota inválida.")
        else:
            # menor nota sem usar função
            menor_nota = nota1

            if nota2 < menor_nota:
                menor_nota = nota2

            if nota3 < menor_nota:
                menor_nota = nota3

            media_nota = (nota1 + nota2 + nota3 - menor_nota) / 2
            print(f"Sua média semestral é: {media_nota}")

            if media_nota < 4:
                print("Você está reprovado direto.")

            elif media_nota >= 7:
                print("Você está aprovado direto.")

            else:
                nota_exame = float(input("Digite a nota do exame: "))

                if nota_exame < 0 or nota_exame > 10:
                    print("Nota inválida.")
                else:
                    media_exame = (nota_exame + media_nota) / 2

                    if media_exame < 5:
                        print(f"Reprovado em exame com média: {media_exame}")
                    else:
                        print(f"Aprovado em exame com média: {media_exame}")