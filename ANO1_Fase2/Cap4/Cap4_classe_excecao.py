# EXCEPTION É A CLASSE BASE DE EXCEÇÃO NO PYTHON
class IdadeMaximaExcedida (Exception):
    # STR É O METODO CHAMADO QUANDO O OBJETO DA CLASSE É CONVERTIDO EM UMA STRING, PODE SER SUBSCRITO PRA PERSONALIZAR A MSG
    def __str__(self):
        return "A idade não pode ser superior a 125 anos"

try:
    idade = int(input("Insira sua idade: "))
    if idade < 0:
        # RAISE GERA ARTIFICIALMENTE UMA EXCEÇÃO
        raise ValueError("Valor de idade não pode ser menor que zero!")
    elif idade > 125:
        raise IdadeMaximaExcedida
except ValueError as error:
    print("Erro: ", error)
# TRATAMENTO DE EXCEÇÃO FAZ NÃO APARECER MENSAGEM VERMELHA AO DIGITAR MAIS DE 125 ANOS
except IdadeMaximaExcedida as error:
    print("Erro: ", error)

# TRATAMENTO GENÉRICO
# except Exception as error:
#    print("Aconteceu um erro: ", error)
else:
    print(f"Você tem {idade} anos")