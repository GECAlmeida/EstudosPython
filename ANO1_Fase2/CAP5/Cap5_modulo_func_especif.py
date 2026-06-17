# IMPORTANDO FUNÇÕES ESPECÍFICAS DO MÓDULO
from calculadora import somar, subtrair

valor1 = float(input("Digite um numero: "))
valor2 = float(input("Digite outro numero: "))
soma = somar(valor1, valor2)
print(soma)

# TAMBEM É POSSIVEL IMPORTAR TODAS ESPECIFICAS DE UMA VEZ, MAS PODE DEIXAR LENTO
# from calculadora import *