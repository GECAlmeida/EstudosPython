import csv
dados_jedi = ['Yoda', '900', 'Mestre']
with open('jedis.csv', mode='a', newline='') as arquivo_csv: # newline='' → evita que o python coloque uma linha em branco entre cada linha do arquivo, significa "nao faca nenhum tratamento especial com as quebras de linha"
    escritor_csv = csv.writer(arquivo_csv, delimiter=',') # depois de Yoda, coloca uma virgula, e assim por diante
    escritor_csv.writerow(dados_jedi) # write row → escreve uma linha no arquivo, no caso, a lista dados_jedi
    
