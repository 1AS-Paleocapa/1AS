
somma = 0
cont = 0

for c in range(1,7):
    n = int(input("Digita il {}° numero intero: " .format(c)))
    if n % 2 == 0:
        cont += 1
        somma += n

print("=" * 40)
print("Hai inserito {} numeri pari e la somma di esse è uguale a {}." .format(cont, somma))
print("=" * 40)
