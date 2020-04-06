from datetime import date
anno = int(input("Digita l'anno che ti interessa (0 per l'anno attuale) : "))
print("-=-" * 20)
if anno == 0:
    anno = date.today().year
if anno%4 == 0 and anno % 100 != 0 or anno % 400 == 0:
    print("L'anno {} è bisestile" .format(anno))
else:
    print("L'anno {} non è bisestile." .format(anno))
print("-=-" * 20)
