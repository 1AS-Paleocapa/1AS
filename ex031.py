dist = int(input("Digita la distanza del tuo viaggio: "))
print("-=" * 20)
if dist <= 200:
    p = dist * 0.50
    print("Il prezzo del tuo biglietto è di {:.2f}€." .format(p))
else:
    p = dist * 0.45
    print("Il prezzo del tuo biglietto è di {:.2f}€.".format(p))
print("-=" * 20)

#p = dist * 0.50 if dist <= 200 else dist * 0.45
#print("Il prezzo del tuo biglietto è di {:.2f}€.".format(p))
