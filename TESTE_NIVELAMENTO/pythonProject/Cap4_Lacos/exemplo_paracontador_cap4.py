num = int(input("Digite 5 números: "))
maior = num


for cont in range (1, 5, 1): # 5 demarca que o quinto é o fim, ou seja, dá somente mais 4 voltas. (começa em 1, 4 voltas, 1 incremento)
    num = int(input()) # não precisa exibir de novo a mensagem
    if num > maior:
        maior = num
print("Maior valor: ", maior)

