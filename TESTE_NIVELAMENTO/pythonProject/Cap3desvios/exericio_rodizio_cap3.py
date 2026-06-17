nplaca = int(input("Digite o número da placa: "))

finalplaca = nplaca % 10 # DIVISÃO POR 10 DESSA FORMA RETONRA O ULTIMO NUMERO INTEIRO QUE RESTOU

if finalplaca == 1 or finalplaca == 2:
    print("Segunda-feira")
elif finalplaca == 3 or finalplaca == 4:
    print("Terça-feira")
elif finalplaca == 5 or finalplaca == 6:
    print("Quarta-feira")
elif finalplaca == 7 or finalplaca == 8:
    print("Quinta-feira")
elif finalplaca == 9 or finalplaca == 0:
    print("Sexta-feira")
