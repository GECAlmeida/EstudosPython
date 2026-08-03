from pathlib import Path
import csv

arquivo = Path(__file__).parent / 'jedis.csv'

dados_jedi = [['Yoda', '900', 'Mestre Jedi'], ['Luke Skywalker', '23', 'Padawan']]
with open(arquivo, mode='a', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=',')
    for linha in dados_jedi:
        escritor_csv.writerow(linha)
