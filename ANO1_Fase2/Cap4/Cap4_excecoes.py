# TRATAMENTO DE EXCEÇÕES
# EXECUCAO DE CÓDIGO QUE PODE DAR ERRO
try:
    idade = int(input("Digite a idade: "))
    idade_amigo = (input("Digite a idade do amigo: ")) # ERRO PROPOSITAL - TYPEERROR
    #idade_total = idade + idade_amigo
    idade_total =  5/0 # ERRO PROPOSITAL - DIVISAO POR 0

# CAPTURA  O ERRO (NO CASO, ERRO DE VALOR) E EXECUTA UM CÓDIGO ALTERNATIVO
except ValueError:
    print("Digite um número inteiro! ")

except TypeError: # POR QUE idade_amigo NÃO ESTÁ DECLARADO COMO INT
    print("Estamos com problemas técnicos, tentando somar inteiro com string. Aguarde a correção do código")

except Exception  as error: # CAPTURA ERRO GENÉRICO (EXCEPTION - CLASSE BASE) QUE NÃO CONSEGUIMOS TRATAR ANTES
    print("Aconteceu um erro ", error)
# EXECUTA SOMENTE SE NÃO HOUVER ERRO, COMO SE O TRY FOSSE UM IF
else:
    print("Idade: ", idade)
    print("Idade  do amigo: ", idade_amigo)
    print("Idade total: ", idade_total)
# SEMPRE É EXECUTADO, INDEPENDENTE DE ERRO OU NÃO
finally:
    print("Obrigado por usar o programa!")