from random import shuffle
a1 = str(input("Digita il nome del primo allievo: "))
a2 = str(input("Digita il nome del secondo allievo: "))
a3 = str(input("Digita il nome del terzo allievo: "))
a4 = str(input("Digita il nome dell'ultimo allievo: "))
list = [a1, a2, a3, a4]
shuffle(list)
print("-" * 80)
print("L'ordine di presentazione è:")
print(list)
print("-" * 80)
