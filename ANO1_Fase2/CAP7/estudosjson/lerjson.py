import json

arquivo = open("C:\\Users\\gabri\\datascience\\EstudosPython\\ANO1_Fase2\\CAP7\\estudosjson\\agenda.json", "r")

conteudo_do_arquivo = arquivo.read() # read() LÊ O CONTEÚDO DO ARQUIVO

agenda = json.loads(conteudo_do_arquivo) # LOADS CONVERTE O JSON EM DICIONARIO

arquivo.close()

print(f"O tipo do objeto agenda é {type(agenda)}") # OU {agenda.__class__}
print(agenda)