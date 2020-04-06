from random import choice
a1 = str(input("Digita il nome del primo allievo: "))
a2 = str(input("Digita il nome del secondo allievo: "))
a3 = str(input("Digita il nome del terzo allievo: "))
a4 = str(input("Digita il nome dell'ultimo allievo: "))
list = [a1, a2, a3, a4]
r = choice(list)
print("-" * 80)
print("L'allievo fortunato è: {}".format(r))
print("-" * 80)
