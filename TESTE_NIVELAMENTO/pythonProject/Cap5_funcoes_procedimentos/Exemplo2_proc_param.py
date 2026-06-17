def saudacao(usuario, hora):
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    print(msg,", ", usuario, ", seja bem-vindo à FIAP!")

saudacao("Gabriel", 11)
