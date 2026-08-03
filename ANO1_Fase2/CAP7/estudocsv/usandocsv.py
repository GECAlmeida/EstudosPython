import csv

# delimiter="," → separa as colunas.
# quotechar='"' → protege textos que têm vírgula dentro deles. por exemplo: Luke Skywalker,23,"Padawan, aprendiz" - com wuotechar = '"' entende que é um elemento só ao invés de dois
with open('jedis.csv') as arquivo_csv: # ou ('jedis.csv', 'r') dá na mesma - padrão
    # FUNCAO READER(parametros file, delimiter, quotechar)
    leitor_csv = csv.reader(arquivo_csv, delimiter = ',', quotechar = '"') # , indica que colunas são separadas por virgula e " indica que " delimita as colunas (caso tenha)
    next(leitor_csv) # IGNORA A PRIMEIRA LINHA, QUE CONTEM APENAS OS TITULOS DAS COLUNAS

    for linha in leitor_csv:
        mensagem = f"O Jedi de nome {linha[0]}, com {linha[1]} anos de idade, é classificado como {linha[2]}."
        print(mensagem)