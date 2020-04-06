"""Calcolo fatibilità di un mutuo"""

# input

importo = float(input("Quanto costa l'immobile che vuoi acquistare? €"))
stipendio = float(input("A quanto ammonta il tuo stipendio netto? €"))
tempo = int(input("In quanti anni vuoi pagare il mutuo?"))

# processing

rata = importo / (tempo * 12)
rata_max = stipendio * 30 / 100

# colors

colors = {"clear": "\33[m",
          "green": "\33[1;32m",
          "red": "\33[1;31m"}
# output

if rata <= rata_max:
    print("{}".format(colors["green"]) + "=" * 60)
    print("CONGRATULAZIONI! La tua richiesta è stata accettata.\n"
          "Il tuo mutuo consiste in {:.0f} rate da {:.2f}€." .format(tempo * 12, rata))
    print("=" * 60 + "{}".format(colors["clear"]))
else:
    print("{}".format(colors["red"]) + "=" * 60)
    print("Purtroppo la tua richiesta non può essere accolta.")
    print("=" * 60 + "{}".format(colors["clear"]))
