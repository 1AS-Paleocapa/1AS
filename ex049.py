from time import sleep

n = int(input("Digita un numero: "))

print("=" * 40)

for c in range(1, 11):
    print("{} X {} = {}".format(n, c, n * c))
    sleep(0.4)

print("=" * 40)
