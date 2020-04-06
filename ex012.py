prezzo = float(input("Digita il prezzo del prodotto: "))
sconto = float(input("Digita la percentuale di sconto da applicare: "))
calc_sconto = (prezzo * sconto) / 100
prezzofinale = prezzo - calc_sconto
print("Il prezzo finale del prodotto è: {:.2f}€".format(prezzofinale))
