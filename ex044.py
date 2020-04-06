"""metodo di pagamento"""

# data

# input

importo = float(input("Digita il costo del prodotto: "))
metodo = int(input("\n"
                   "1 - In Contanti / Bancomat / Carta di Credito\n"
                   "2 - 2 rate\n"
                   "3 - 3 rate\n"
                   "\n"
                   "Come preferisci pagare: "))

# processing

saldo = importo - (importo / 100 * 10)
duerate = importo
trerate = importo + (importo / 100 * 20)

# colors

# output

print("=" * 60)
if metodo == 1:
    print("Il prezzo totale da pagare è {:.2f}€".format(saldo))
elif metodo == 2:
    print("Il prezzo totale da pagare è {:.2f}€".format(duerate))
elif metodo == 3:
    print("Il prezzo totale da pagare è {:.2f}€".format(trerate))
else:
    print("ERRORE: Metodo di pagamento non valido")
print("=" * 60)
