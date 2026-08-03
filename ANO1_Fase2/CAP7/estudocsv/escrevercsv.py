import os
from pathlib import Path
import csv

print(os.getcwd())

arquivo = Path(__file__).parent / 'jedis.csv' # Path(__file__) → pega o caminho do arquivo atual, parent → pega o caminho da pasta que contem o arquivo atual, / 'jedis.csv' → cria um caminho para o arquivo jedis.csv dentro da pasta atual
dados_jedi =  ['Yoda', '900', 'Mestre']

print("Arquivo que seá alterado: ")
print(arquivo.resolve())

with open(arquivo, mode='a', newline='') as arquivo_csv: # newline='' → evita que o python coloque uma linha em branco entre cada linha do arquivo, significa "nao faca nenhum tratamento especial com as quebras de linha"
    escritor_csv = csv.writer(arquivo_csv, delimiter=',') # depois de Yoda, coloca uma virgula, e assim por diante
    escritor_csv.writerow(dados_jedi) # write row → escreve uma linha no arquivo, no caso, a lista dados_jedi
