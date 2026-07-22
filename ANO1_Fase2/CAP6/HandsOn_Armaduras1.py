# ARMADURAS INICIAIS
nomes_armaduras = ['Mark I','Mark III', 'Mark V', 'Mark II', 'Mark IV']
print(f'Catálogo de armaduras: {nomes_armaduras}')

# ADICIONANDO ARMADURA
nomes_armaduras.append(input('Digite o nome da nova armadura: '))
print(f'Catálogo atualizado: {nomes_armaduras}\n')

# ESCOLHENDO POSIÇÃO
print(f'Posições disponíveis: {len(nomes_armaduras)}')
nova_armadura = input('Digite o nome da nova armadura: ')
while True:
    posicao = int(input('Digite a posição da nova armadura: '))
    if posicao >= 0 and posicao <= len(nomes_armaduras):
        break
    print(f"Digite uma posição entre 0 e {len(nomes_armaduras)}")
nomes_armaduras.insert(posicao, nova_armadura)
print(f'Catálogo atualizado: {nomes_armaduras}\n')

#ORDENANDO LISTA EM ORDEM ALFABÉTICA
nomes_armaduras.sort()
print(f"Lista ordenada: {nomes_armaduras}\n")
nomes_armaduras.sort(reverse=True)
print(f"Lista ordenada reversa: {nomes_armaduras}\n")
# IGNORANDO MAIUSCULAS E MINUSCULAS
nomes_armaduras.sort(key=str.lower)
print(nomes_armaduras,"\n")

# USANDO SLICING - INTERVALO
print("Escolha um intervalo de armaduras para exibir")
inicio = int(input("Posição inicial: "))
fim = int(input("Posição final: "))
print(nomes_armaduras[inicio:fim]) # OU CRIAR VARIAVEL: intervalo = nomes_armaduras[inicio:fim]

# TUPLA PARA LISTAR CARACTERISTICAS
caracteristicas_armaduras = (
    ('Ferro', 'Pequena', 200),
    ('Titânio', 'Média', 300),
    ('Liga Metálica', 'Média', 400),
    ('Fibra de Carbono', 'Grande', 500),
    ('Ouro', 'Pequena', 600),
    (input('Digite o material da nova armadura: '), input('Digite o tamanho: '), int(input('Digite o peso:')))
)
print('Características das armaduras: ', caracteristicas_armaduras)

# CONTANDO VEZES QUE MATERIAL APARECE
material = input('Digite o material que quer contar: ')
quantidade = 0
for armaduras in caracteristicas_armaduras:
    if armaduras[0] == material:
# OUTRA FORMA, transformando cada um em indice da tupla:
# for i in range(len(caracteristicas_armaduras)):
#   if caracteristicas_armaduras[i][0] == material:
        quantidade += 1
print('Quantidade de armaduras com o material:', quantidade)


print("Criando o dicionário \n")
# DICIONARIO = {CHAVE: VALOR, CHAVE:{VALOR}} ETC
informacoes_armaduras = {
    'Mark I': {'ano': 2008, 'proteção': 'baixa', 'potência de fogo': 10},
    'Mark II': {'ano': 2010, 'proteção': 'média', 'potência de fogo': 20},
    'Mark III': {'ano': 2012, 'proteção': 'média', 'potência de fogo': 30},
    'Mark IV': {'ano': 2013, 'proteção': 'alta', 'potência de fogo': 40},
    'Mark V': {'ano': 2014, 'proteção': 'alta', 'potência de fogo': 50},
}

print("Obtendo a lista de tuplas (chave, valor) usando metodo items()")
lista_tuplas = informacoes_armaduras.items()
print("Informações, lista de tuplas: ", lista_tuplas)

#ATUALIZANDO USANDO UPDATE
print("Armaduras disponíveis: ", list(informacoes_armaduras.keys()))
armadura = input("Nome: ")
ano = input("Ano: ")
protecao = input("Proteção: ")
potencia = input("Poência: ")

informacoes_armaduras.update({armadura: {'ano': ano,'proteção': protecao,'potência de fogo': potencia}})
print('\n Informações da amadura', armadura, ' atualizadas: ', informacoes_armaduras[armadura])

# REMOVENDO ARMADURA DO DICIONÁRIO
armadura  = input('Digite o nome da armadura que deseja remover ' + str(list(informacoes_armaduras.keys())) + ': ')
# OU MAIS PYTHONICO:
# armadura = input(f'Digite o nome da armadura que deseja remover {list(informacoes_armaduras.keys())}: ')
informacoes_armaduras.pop(armadura)

#Apresentando dicionário atualizado
print('\n Dicionário atualizado: \n')
for chave, valor in informacoes_armaduras.items():
    print(chave, valor)
    # OU TAMBÉM:
    print('Nome:', chave)
    print('Ano de lançamento:', valor['ano'])
    print('Nível de proteção:', valor['proteção'])
    print('Potência de fogo:', valor['potência de fogo'])
    print('')  # linha em branco para separar as informações de cada armadura
