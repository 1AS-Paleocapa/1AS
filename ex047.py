"""tutti i numero pari da 1 a 50"""

from time import sleep

for cont in range(2, 51, 2):
    #if cont % 2 == 0:
    print(cont, end=" ")
    sleep(0.4)

print("FINE")