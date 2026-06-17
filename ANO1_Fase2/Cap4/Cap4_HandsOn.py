# CRIAÇÃO DA CLASSE DE EXCEÇÃO
class NumerosNegativos(Exception):
    def __str__(self):
        return "Você informou um número negativo!"
try:
    vl_total = float(input("Qual valor total da compra? "))
    qtd_itens = int(input("Qual total de itens? "))
    if vl_total < 0 or qtd_itens < 0:
# PROPAGAÇÃO DA EXCEÇÃO
        raise NumerosNegativos
    # ROUND ARREDONDA
    media = round(vl_total/qtd_itens)
except ZeroDivisionError:
    print("Divisão por zero! A quantidade de itens deve ser maior que 0! ")
except ValueError:
    print("Entre com um número! ")

# TRATAMENTO DA EXCEÇÃO CRIADA
except NumerosNegativos as error:
    print(error)
else:
    print(f"Valor total: R$ {vl_total:.2f}; Quantidade de Itens: {qtd_itens}; Valor médio por item: {media:.2f}")
finally:
    print("Continue acompanhando seus gastos!")