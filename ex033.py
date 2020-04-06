a = int(input("Digita il primo numero: "))
b = int(input("Digita il secondo numero: "))
c = int(input("Digita il terzo numero: "))
minore = a
if b < a and b < c:
    minore = b
if c < a and c < b:
    minore = c
maggiore = a
if b > a and b > c:
    maggiore = b
if c > a and c > b:
    maggiore = c
print("-=" * 20)
print("Il numero minore è {}.".format(minore))
print("Il numero maggiore è {}.".format(maggiore))
print("-=" * 20)
