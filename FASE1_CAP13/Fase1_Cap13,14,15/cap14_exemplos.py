"""
# Formatação \n pula linhas e \t equivale a tabulação ou espaço dado com tab
print("Saudações Jedi\nViemos numa missão de\tpaz")
"""

"""
#Com código de cores padrão ANSI
print("Saudações\033[1;35;40mJedi\033[0m\nViemos numa missão de\t\033[1;32;40mpaz\033[0m")
"""

"""
# Converter tipo numerico para alfanumerico para concatenar
nome = Gabriel
x = 10
nome + str(x)
# ou...
z = "5"
int(z)
"""

"""
# Transformando a variável em inteiro para ser recebida, da mesma forma pode se tornar se: x = int(x)
x = int(input("Entre com um número "))
print(x)
print(type(x))
"""

"""
nome = input("Entre com o seu nome: ")
print(nome)
sobrenome = input("Entre com o seu sobrenome: ")
print(sobrenome)
print(nome + " " + sobrenome)
"""

"""
ano = 1989
nome = "Luke Skywalker"
saldo = 50.30
# {} é um marcador de posição na string e .format é o metodo chamado na string e recebe os argumentos/valores
print(("O tipo da variável ano é {}".format(type(ano))))
print(("O tipo da variável nome é {}".format(type(nome))))
print(("O tipo da variável saldo é {}".format(type(saldo))))
"""

"""
nome = "Maria"
idade = 30
mensagem = "{} tem {} anos.".format(nome, idade)
print(mensagem)
"""

"""
# O codigo de cor vermelha \033[1;31m e o código para retomar a cor \033[0m
print("Ola mundo\nComo vai \t\033[1;31mvoce\033[0m")
print("Como voce se chama")
"""

"""
# FORMATAÇÃO DE ALFA NUMÉRICO - PREENCHER, ALINHAR, LARGURA E PRECISÃO
# Centralizar em 20 posições :^20, se fosse a esquerda :<20 ou a direita :>20
nome = input("Entre com seu nome ")
# saudacao = "Bem-vindo {:*^20}".format(nome)
# print(saudacao)
idade = input("Entre com sua idade ")
# saudacao = "Bem-vindo {:*^20}. Você tem {:#<10}".format(nome, idade)
# Uma forma de posicionar as variáveis como quiser mesmo que troque a ordem no format é colocar variaveis dentro das chaves
saudacao = "Bem-vindo {var1:*^20}. Você tem {var2:#<10}".format(var1=nome, var2=idade)
print(saudacao)
"""

"""
# Outro exemplo, colocando a formatação na variável
saudacao = 'Bem-vindo {nome}! Você chegou em {lugar}. '            'Prossiga para o controle {inspecao}'.format(lugar='Alderaan', nome="Jedi", inspecao="area 4")
print(saudacao)
"""
"""
numero = float(input("entre com o numero"))
# retornará 10 posições e 5 casas decimais após a vírgula - param foi exemplo, mas pode nomear a chave como quiser
# print("Seu numero é {param:10.5f}".format(param=numero))

#usando f strings ao invés de format
print(f"Seu numero é {numero:10.5f}")
"""


