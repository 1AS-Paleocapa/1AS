larg = float(input("Digita la larghezza del muro: "))
alt = float(input("Digita l'altezza del muro: "))
area = larg * alt
resa = 2
totale = area / resa
print("-" * 40)
print("Per un muro di {:.2f} m², consideranto la resa di {} litri/m², avrai bisogno di {:.0f} litri di pittura.".format(area, resa, totale))
print("-" * 40)
