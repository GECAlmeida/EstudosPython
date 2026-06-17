# IMPORTAÇÃO DE MÓDULO CRIADO
import calculadora

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

#REFERENCIANDO MODULO CRIADO E USANDO UMA FUNÇÃO INTERNA
print(calculadora.somar(n1,n2))
