'''Calcolo dell'insteresse composto'''

# dati

ci = float(input("Digita il tuo capitale iniziate: "))
tasso = float(input("Digita il tasso d'interesse annuo: "))
durata = int(input("Digita la durata dell'investimento in mesi: "))

# elaborazione

tasso = tasso / 100
durata = durata / 12
cf = ci * (1 + tasso) ** durata

# colors

colors = {"clear": "\33[m",
          "start": "\33[1;30;31m"}

# output

print("{}".format(colors["start"]))
print("=" * 40)
print("CAPITALE INVESTITO: {:.2f} €\n"
      "TASSO ANNUO: {:.1f} %\n"
      "DURATA: {:.0f} mesi\n"
      "INTERESSI MATURATI: {:.2f} €\n"
      "CAPITALE FINALE: {:.2f} €".format(ci, tasso * 100, durata * 12, cf - ci, cf))
print("=" * 40)
print("{}".format(colors["clear"]))
