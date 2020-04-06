num = int(input("Digita un numero da 0 a 9999: "))

#n = str(num)
#print("-" * 80)
#print("Unità: {}".format(n[3]))
#print("Decina: {}".format(n[2]))
#print("Centinaia: {}".format(n[1]))
#print("Migliaia: {}".format(n[0]))
#print("-" * 80)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("-" * 80)
print("Unità: {}".format(u))
print("Decina: {}".format(d))
print("Centinaia: {}".format(c))
print("Migliaia: {}".format(m))
print("-" * 80)
