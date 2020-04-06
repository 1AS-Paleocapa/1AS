"""La somma di tutti i numero tra 0 e 500, dispari e multipli di 3."""

somma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        somma += c
        cont += 1

print("=" * 40)
print("La somma dei {} numeri è {}." .format(cont, somma))
print("=" * 40)
