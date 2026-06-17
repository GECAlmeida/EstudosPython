# há 3 formas de exibir dados com print:
# 1- separando os termos com vírgula (,)
# 2- utilizando função format()
# 3- utilizando print(f"")

nome = "Gabriel"
idade = 21
peso = 71.52

# forma 1
print("1. O meu nome é ",nome,", tenho ",idade," anos e ",peso," quilos")

# forma 2
print("2. O meu nome é {} tenho {} anos e {} quilos".format(nome, idade, peso))
print("2. O meu nome é {0} tenho {1} anos e {2:.1f} quilos".format(nome, idade, peso))
print("2. O meu nome é {n} tenho {i} anos e {p:.2f} quilos".format(n=nome,i=idade,p=peso))

# forma 3 - f no começo indica que é uma f-string e traz a formatação colocando as variáveis dentro das {}
print(f"3. O meu nome é {nome}, tenho {idade} anos e {peso:.2f} quilos")

