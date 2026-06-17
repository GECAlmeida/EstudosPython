def fsaudacao(pPeriodo, *pNome):
    for i in pNome:
        if pPeriodo.lower() in ("manhã", "manha", "m"):
            print(f"Bom dia, {i}! Como vai?")
        elif pPeriodo.lower() in ("tarde", "t"):
            print(f"Boa tade, {i}! Como vai?")
        elif pPeriodo.lower() in ("noite", "n"):
            print(f"Boa noite, {i}! Como vai?")
        else:
            print(f"Olá, {i}! Como vai?")
fsaudacao("n", "Gabriel", "João", "Maria")