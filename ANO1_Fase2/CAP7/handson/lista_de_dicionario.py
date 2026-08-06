import json

# abrindo o arquivo agenda.json que é lista de dicionário para leitura
with open("C:\\Users\\gabri\\datascience\\EstudosPython\\ANO1_Fase2\\CAP7\\handson\\agenda_dc.json", "r") as arquivo:

    conteudo_arquivo = arquivo.read() # read() LÊ O CONTEÚDO DO ARQUIVO

    lista = json.loads(conteudo_arquivo) # LOADS CONVERTE O JSON EM DICIONARIO OU LISTA DE DICIONARIOS

# for dicionario percorre cada dicionaio da lista: Bruce Wayne, Clark Kent...
for dicionario in lista:
    # for chave, valor percore cada chave (ex.: Celular, Email) e valor (ex.: 123456)
    for chave, valor in dicionario.items():
        print(f"{chave} ---- {valor}")
