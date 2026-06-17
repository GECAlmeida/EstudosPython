# FUNÇÃO
def calc_vel_med(dist, temp):

    vel_media = dist/temp
    return f"Velocidade média: {vel_media:.2f}"

#PROGRAMA PRINCIPAL
distancia = float(input("Distancia: "))
tempo = float(input("Tempo: "))
# mensagem = calc_vel_med(distancia, tempo)
# print(mensagem)
# OU JEITO MAIS ENXUTO ABAIXO
print(calc_vel_med(distancia, tempo))