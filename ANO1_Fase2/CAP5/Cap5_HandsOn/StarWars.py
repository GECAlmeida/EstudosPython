verifica_atmosfera = lambda planeta: "Atmosfera respirável" if planeta != "Hoth" else "Não respirável"
print(list(map(verifica_atmosfera, ["Tatooine", "Hoth", "Endor", "Alderaan", "Nsboo"])))

