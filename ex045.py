"""Morra cinese"""

from random import randint
from time import sleep

elenco = ("CARTA", "SASSO", "FORBICE")
pc = randint(0, 2)

user = int(input("\n"
                 "0 - CARTA\n"
                 "1 - SASSO\n"
                 "2 - FORBICE\n"
                 "\n"
                 "Scegli la tua opzione: "))

print("SASSO")
sleep(.33)
print("CARTA")
sleep(.33)
print("FORBICE")
sleep(.33)

if user == 0:
    scelta = "CARTA"
elif user == 1:
    scelta = "SASSO"
elif user == 2:
    scelta = "FORBICE"
else:
    print("=" * 60 + "\n"
                     "ERROR: E' stata rilevata una scelta non valida.")
    print("=" * 60)
    exit()

if pc == 0:
    if user ==  0:
        results = "PAREGGIO"
    elif user == 1:
        results = "HAI PERSO"
    else:
        results = "HAI VINTO"

elif pc == 1:
    if user ==  0:
        results = "HAI VINTO"
    elif user == 1:
        results = "PAREGGIO"
    else:
        results = "HAI PERSO"

elif pc == 2:
    if user ==  0:
        results = "HAI PERSO"
    elif user == 1:
        results = "HAI VINTO"
    else:
        results = "PAREGGIO"

print("=" * 60)
print("Il PC ha scelto: {}\n"
      "Tu hai scelto: {}".format(elenco[pc], scelta))
print("=" * 60)
print(results)
print("=" * 60)
