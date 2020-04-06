from math import pow, sqrt, hypot
co = float(input("Digita la lunghezza del cateto opposto: "))
ca = float(input("Digita la lunghezza del cateto adiacente: "))

#i = pow(co, 2) + pow(ca, 2)
#i = sqrt(i)

i = hypot(co, ca)

print("La tua ipotenusa é {:.2f}.".format(i))