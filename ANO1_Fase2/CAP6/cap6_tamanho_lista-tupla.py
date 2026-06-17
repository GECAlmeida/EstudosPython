import sys

nome = "Bruce Wayne"
idade = 30
peso = 92.3

# EXIBIR NOME DA VARIAVEL, TIPO (TYPE) E O TAMANHO (GETSIZEOF)
print("A variavel nome é do tipo {} e tem {} bytes".format(type(nome), sys.getsizeof(nome)))
print("A variavel idade é do tipo {} e tem {} bytes".format(type(idade), sys.getsizeof(idade)))
print("A variavel peso é do tipo {} e tem {} bytes".format(type(peso), sys.getsizeof(peso)))
print(f"A variavel nome é do tipo {type(nome)} e tem {sys.getsizeof(nome)} bytes")

lista_vazia = []
tupla_vazia = ()
print("\nO objeto lista_vazia é do tipo {} e ocupa {} bytes na memória".format(type(lista_vazia), sys.getsizeof(lista_vazia)))
print("O objeto tupla_vazia é do tipo {} e ocupa {} bytes na memória".format(type(tupla_vazia), sys.getsizeof(tupla_vazia)))