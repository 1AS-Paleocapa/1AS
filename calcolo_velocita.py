"""Calcolo della velocità in km/h e m/s"""

# dati

dist = float(input("Per quanti km hai corso? "))
min = int(input("In quanti minuti? "))

# elaborazione

m = dist * 1000  # da km a metri
s = min * 60  # da minuti a secondi
v = m / s

# colors

colors = {"clear": "\33[m",
          "start": "\33[1;30;31m"}

# output

print("{}".format(colors["start"]))
print("=" * 75)
print("Hai corso {} km in {} minuti. La tua velocià media è di {} m/s." .format(round(dist, 1), min, round(v, 1)))
print("=" * 75)
print("{}".format(colors["start"]))
