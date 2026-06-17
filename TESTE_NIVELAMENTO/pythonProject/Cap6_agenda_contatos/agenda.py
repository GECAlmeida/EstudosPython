agenda = [] # Criando uma lista vazia


# DEFINIÇÃO DAS FUNÇÕES

# PROCEDIMENTO QUE LÊ UM NOME
def p_nome():
    return(input("Nome...: "))


# PROCEDIMENTO QUE CRIA UM NOVO CONTATO NA AGENDA
# Nome: novo()
# tipo: procedimento
def novo():
    nome = p_nome()
    celular = input("Celular...: ")
    email = input("E-mail...: ")
    agenda.append([nome, celular, email]) #Adicionando os dados na agenda
    print("\n_______________________________\n Registro gravado com sucesso! ")


# PROCEDIMENTO QUE LISTA UM REGISTRO
def listar_dados(nome, celular, email):
    print(f"Nome: {nome}\nCelular: {celular}\nE-mail: {email}")
    print("________________________________________")


# PROCEDIMENTO QUE LISTA TODOS OS REGISTROS DA MATRIZ
def listar():
    print("\nCONTATOS DA AGENDA ############")
    for e in agenda:
        listar_dados(e[0], e[1], e[2])
    print("\nFIM DA AGENDA ##########\n")


# FUNÇÃO QUE PESQUISA UM CONTATO PELO NOME
def pesquisa(nome):
    name = nome.lower()
    for d, e in enumerate(agenda): # PERCORRE TODA MATRIZ -   d É O INDICE, e É O ELEMENTO
        if e[0].lower() == name: # PROCURA O NOME DESEJADO, e[0] EQUIVALE AOS NOMES ARMAZENADOS, [1] É TELEFONE, ETC
            return d # RETORNA O INDICE DO NOME ENCONTRADO
    return None # RETORNA VAZIO SE NÃO ENCONTRAR


# PROCEDIMENTO QUE EXIBE O REGISTRO OU MENSAGEM DE INSUCESSO
def pesquisar():
    p = pesquisa(p_nome()) # Entrada de dados
    if p != None:
        print("Registro encontrado!")
        # atualiza as variaveis se encontrou
        nome = agenda[p][0]
        celular = agenda[p][1]
        email = agenda[p][2]
        # mostra o registro
        listar_dados(nome, celular, email)
    else:
        print("\nNome não encontrado!")


# PROCEDIMENTO QUE APAGA UM CONTATO
def apagar():
    global agenda #PRA CHAMAR VARIAVEL FORA DO PROCEDIMENTO SE PRECISAR MODIFICÁ-LA
    nome = p_nome()
    #retorna o índice do nome ou vazio
    p = pesquisa(nome)
    if p != None: #Se encontrou o contato
        del agenda[p]
        print("\n_______________________________\nRegistro APAGADO com sucesso!")
    else:
        print("Nome não encontrado.")


# PROCEDIMENTO QUE EDITA UM CONTATO
def editar():
    p = pesquisa(p_nome()) # Entrada de dados
    # Se encontrou o registro
    if p != None:
        # Mostra o nome e pede a edição dos demais
        nome = agenda[p][0]
        print("Nome...:", nome)
        celular = input("Celular...: ")
        email = input("E-mail...:")
        agenda[p] = [nome,celular, email] # Armazenando os novos dados.
        print("\n______________________________\nRegistro EDITADO com sucesso!\n__________________________________")
    else:
        print("Nome não encontrado.")


# FUNÇAO QUE VALIDA SE O ITEM DIGITADO FOI VALIDO
def validar(pergunta, inicio, fim):
    while True: # Criando um loop infinito
        try: #Criando um acordo/condição
            valor = int(input(pergunta)) #Entrada de dados
            if valor <= fim: #Determinando uma condição
                return (valor) #Executa caso for verdadeira)
            else:
                return(0)
        except ValueError: #Executa caso for falsa.
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")


# FUNÇÃO QUE RETORNA O ITEM DO MENU OU 0 PARA INVÁLIDO
def menu(): # Exibe o menu de opções
    print("""
    1 - Adicionar novo contato
    2 - Editar um contato
    3 - Pesquisar contato
    4 - Lista de contatos
    5 - Apagar um contato
    6 - Sair
""")
    return validar("Escolha uma opção: ", 1, 6)


# PROGRAMA PRINCIPAL
while True: # Criando looping infinito
    opcao = menu()
    if opcao == 0:
        print("Opção Inválida!")
    elif opcao == 6:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        pesquisar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        apagar()
    else:
        print("Opção Inválida!")