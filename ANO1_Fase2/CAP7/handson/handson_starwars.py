import json

# MELHOR PRÁTICA: USAR O ENCODING UTF-8 PARA LER ARQUIVOS JSON PARA EVITAR ERROS DE CODIFICAÇÃO DE CARACTERES ESPECIAIS
with open(
    "C:\\Users\\gabri\\DATA SCIENCE\\EstudosPython\\ANO1_Fase2\\CAP7\\handson\\star_wars.json",
    "r",
    encoding="utf-8"
) as arquivo:
    # MELHOR PRÁTICA: USAR json.load() AO INVES DE json.loads() PARA LER DIRETAMENTE O CONTEÚDO DO ARQUIVO JSON
    lista = json.load(arquivo) #json.load() é como se fosse o json.loads() mas lendo diretamente do arquivo, sem precisar do read()
    # json.loads ---> string / json.load ---> arquivo

# variaveis para contar os generos
masculino = 0
feminino = 0
neutro = 0
# percorre cada dicionario da lista de personagens
for dicionario in lista:
    # EXIBINDO NOME E GENERO DE CADA PERSONAGEM
    print(f"Nome do personagem: {dicionario['name']}")
    # TRADUZINDO O GÊNERO PARA PORTUGUÊS
    if dicionario["gender"] == "male":
        print(f"Gênero: Masculino\n")
    elif dicionario["gender"] == "female":
        print(f"Gênero: Feminino\n")
    elif dicionario["gender"] == "n/a":
        print(f"Gênero: Neutro\n")

# CONTANDO O TOTAL DE PERSONAGENS MASCULINOS, FEMININOS E NEUTROS
    if dicionario["gender"] == "male":
        masculino = masculino + 1
    elif dicionario["gender"] == "female":
        feminino = feminino + 1
    elif dicionario["gender"] == "n/a":
        neutro = neutro + 1
# EXIBINDO O TOTAL  
print(f"Total de personagens masculinos: {masculino}")
print(f"Total de personagens femininos: {feminino}")
print(f"Total de personagens neutros: {neutro}")

# PESQUISANDO DADOS DE UM PERSONAGEM ESPECÍFICO
pesquisa = input("Digite o nome do personagem que deseja pesquisar: ")
for dicionario in lista:
    # SE O NOME FOR IGUAL AO NAME NO DICIONARIO
    if pesquisa.lower() in dicionario["name"].lower():
        print(f"Dados do personagem {pesquisa}:")
        print(f"Nome: {dicionario['name']}")
        print(f"Gênero: {dicionario['gender']}")
        print(f"Altura: {dicionario['height']}")
        print(f"Peso: {dicionario['mass']}")
        print(f"Cor do cabelo: {dicionario['hair_color']}")
        print(f"Cor da pele: {dicionario['skin_color']}")
        print(f"Cor dos olhos: {dicionario['eye_color']}")
        print(f"Ano de nascimento: {dicionario['birth_year']}")