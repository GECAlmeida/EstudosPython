# hora é o parâmetro
def saudacao(hora):
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    print(msg, ", seja bem-vindo à FIAP")

saudacao(11)
