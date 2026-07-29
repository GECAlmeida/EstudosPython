#usando funcao open para criar um obj do tipo arquivo. tem que duplicar barrar pra reconhecerr como barra
arquivo = open('C:\\Users\\gabri\\DATA SCIENCE\\EstudosPython\\ANO1_Fase2\\CAP7\\arquivo_de_texto.txt')
print(type(arquivo))
#  print(arquivo.read())
# LER OS PRIMEIROS 50 BYTES
# print(arquivo.read(50)) # LÊ OS 50 PRIMEIROS, SE FIZER OUTRO READ(50), VAI LER OS 50 PROXIMOS
# arquivo.seek(0) # VOLTA PRO INICIO

# printando uma linha do arquivo
# print(arquivo.readline())
# printando outra
# print(arquivo.readline())

# Exibindo uma linha por vez com loop for
#for linha in arquivo:
#    print (linha, end = "")

# OU com rtrip (RIGHT STRIP - remove o que estiver a direita da string)

#for linha in arquivo.readlines(): # - readlineS faz serem lidas todas linhas
#    print(linha.rstrip('\n'))

# PASSANDO PRA UMA LISTA
linhas_arquivo = arquivo.readlines()
print(type(linhas_arquivo))
linhas_arquivo.sort()
print(linhas_arquivo)