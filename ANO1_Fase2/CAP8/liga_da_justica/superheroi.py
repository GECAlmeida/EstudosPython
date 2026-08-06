# IMPORTANDO STREAMLIT PARA CRIAR A INTERFACE DO USUÁRIO
import streamlit as st
# IMPORTANDO PATHLIB PARA TRABALHAR COM CAMINHOS DE ARQUIVOS
from pathlib import Path

def heroi():
    name = st.text_input("Nome do Herói:") # pede digitacao do nome
    age = st.number_input("Idade do Herói:", value=0, step=1, min_value=0, max_value=9999) # step=1 significa que a cada clique no botão de mais ou menos, o valor aumenta ou diminui 1 unidade
    return name, age

def principal():
    # Criando lista de habilidades
    habilidades = ["Super Força", "Velocidade", "Invisibilidade", "Teletransporte", "Vôo", "Telecinese", "Rajada de Energia", "Controle Mental", "Manipulação do Tempo", "Regeneração", "Elasticidade", "Intangibilidade", "Manipulação da Gravidade", "Manipulação da Realidade", "Manipulação da Mente", "Manipulação da Matéria", "Manipulação da Energia", "Manipulação do Espaço-Tempo", "Sem Poderes", "Outro"]
    # Título e subtítulo do app
    st.title("Cadastro de Super-Heróis")
    st.subheader(" Por favor, informe seus dados abaixo:")

    # PEDIR NOME E IDADE USANDO A FUNCAO
    nome, idade = heroi()

    # Criar lista suspensa com poderes de super-heróis
    habilidade = st.selectbox("Indique sua habilidade:", habilidades)
    if habilidade == "Outro":
        habilidade = st.text_input("Descreva sua habilidade:")

    # Cria um botão pra enviar os dados
    submit = st.button("Enviar dados")

    # SE O BOÃO FOR PRESSIONADO, EXIBE UMA MENSAGEM COM OS DADOS
    if submit:
        st.write("Seus dados foram enviados com sucesso!")
        st.write(f"O novo herói {nome} tem {idade} anos e possui a seguinte habilidade: {habilidade}.")

    #EXIBINDO UMA IMAGEM
    imagemliga = Path(__file__).parent / "justiceleague.png"
    st.image(imagemliga, caption="Liga da Justiça, os heróis mais poderosos da Terra", width=800)

# if __name__ == "__main__": significa que o código dentro do bloco só será executado se o arquivo for executado diretamente, e não importado como módulo em outro arquivo.
if __name__ == "__main__":
    principal()
