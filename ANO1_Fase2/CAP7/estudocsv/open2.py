# CRIANDO VARIAVEL DE TEXTO
conteudo = "Estou testando criar um arquivo de texto."
# CRIANDO novo_arquivo - 'w' é um argumento
# w - write
# r - read - abrir para leitura(padrao)
# x - abrir para criar arquivo
# a - appen - anexar conteudo novo ao final
# b - abrir em modo binario
# t - abrir em modo de texto(padrao)
# + - abrir para atualização (leitura e escrita)

# arquivo = open('C:\\Users\\gabri\\DATA SCIENCE\\EstudosPython\\ANO1_Fase2\\CAP7\\novo_arquivo_de_texto.txt', 'w')
## ESCREVENDO O CONTEUDO DA VARIAVEL CONTEUDO DENTRO DO ARQUIVO
# arquivo.write(conteudo)
# arquivo.close()

arquivo = open('C:\\Users\\gabri\\DATA SCIENCE\\EstudosPython\\ANO1_Fase2\\CAP7\\novo_arquivo_de_texto.txt', 'a')
arquivo.write(conteudo)
arquivo.close()