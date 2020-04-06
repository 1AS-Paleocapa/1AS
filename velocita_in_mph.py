"""nome"""

# data

v_mph = float(1609.344)
conv_mph = float(0.6213711922)
# input

dist = float(input("Quanti km hai percorso? "))
min = int(input("In quanti minuti? "))

# processing

m = dist * 1000  # da km a metri
s = min * 60  # da minuti a secondi
v = m / s
v1 = (dist / min) * 60
mph = v1 * conv_mph

# colors

colors = {"clear": "\33[m",
          "start": "\33[1;30;31m"}

# output

print("{}".format(colors["start"]))
print("=" * 75)
print("Hai percorso {} km in {} minuti.\n"
      "La tua velocià media è di {} m/s.\n"
      "La tua velocià media è di {} km/h.\n"
      "La tua velocità media è di {} mph".format(dist, min, round(v, 2), round(v1, 2), round(mph, 2)))
print("=" * 75)
print("{}".format(colors["start"]))
