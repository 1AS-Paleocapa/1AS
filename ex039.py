"""Calcolo età militare"""

# import

from datetime import date
#from time import strftime

# input

year = int(input("Digita il tuo anno di nascita: "))

# processing

eta = int(date.today().year) - year
#eta = int(strftime("%Y")) - year

# output

print("=" * 60)
if eta == 18:
    print("Quest'anno ti devi arruolare.")
elif eta > 18:
    print("Sei in ritardo per l'arruolamento.")
elif eta == 17:
    print("Troppo presto, ti manca {} anno per l'arruolamento." .format(18 - eta))
else:
    print("Troppo presto, ti mancano {} anni per l'arruolamento." .format(18 - eta))
print("=" * 60)
