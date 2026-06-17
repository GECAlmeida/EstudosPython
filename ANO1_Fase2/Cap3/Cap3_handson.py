total_calorias = 0.0

qtd_alimento = int(input("Digite quantos alimentos você consumiu hoje: "))

for i in range(1, qtd_alimento + 1, 1):
    alimento_calorias = float(input(f"Quantas calorias o alimento {i} possui? "))
    total_calorias += alimento_calorias

print("Você consumiu um total de: ", total_calorias, " calorias hoje!")
