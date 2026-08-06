import streamlit as st

st.title("Meu primeiro app com Streamlit!")
st.subheader("Subtítulo do app")
st.write("Olá Mundo!")
st.image("C:\\Users\\gabri\\datascience\\EstudosPython\\ANO1_Fase2\\CAP8\\liga_da_justica\\justiceleague.png")


# PARA COLOCAR VIDEO DO YOUTUBE NO STREAMLIT:
# components.v1.iframe pega o link do vídeo e coloca no app
# Pegar link do youtube, copiar o código do vídeo (o que vem depois do watch?v= e colar no link do iframe depois do embed/
st.components.v1.iframe(
    "https://www.youtube.com/embed/dQw4w9WgXcQ", 
    # height e width são as dimensões do vídeo
    height=400
)
# PARA EXECUTAR O APP, RODE O COMANDO ABAIXO NO TERMINAL:
# streamlit run C:/Users/gabri/datascience/EstudosPython/ANO1_Fase2/CAP8/streamlittest.py

