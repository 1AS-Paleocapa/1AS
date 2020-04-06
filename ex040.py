"""Media e risultato"""

# data

# input

primo = float(input("Digita il voto del primo quadrimestre: "))
intermedio = float(input("Digita il voto del periodo intermedio: "))
finale = float(input("Digita il voto finale: "))

# processing

media = (primo + intermedio + finale) / 3

# colors

# output

print("=" * 60)
if media > 7:
    print("COMPLIMENTI! Sei stato promosso con una media di {:.1f}.".format(media))
elif media < 5:
    print("Purtroppo sei stato bocciato, la tua media di {:.1f} non è sufficiente.".format(media))
else:
    print("Con una media di {:.1f}, sei stato rimandato in questa materia.".format(media))
print("=" * 60)
