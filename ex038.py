"""Confronto di numeri interi"""

# input

n1 = int(input("Digita un numero intero: "))
n2 = int(input("Digita un'altro numero intero: "))

# processing

# colors

# output

print("\n" + "=" * 60)
if n1 > n2:
    print("Il numero {} è maggiore del numero {}." .format(n1, n2))
elif n1 < n2:
    print("Il numero {} è minore del numero {}." .format(n1, n2))
else:
    print("I numeri scelti sono uguali.")
print("=" * 60)
