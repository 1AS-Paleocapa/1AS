"""Categorie Nuoto"""

# data

from datetime import date
from time import strftime

# input

anno_nascita = int(input("Digita il tuo anno di nascita: "))

# processing

age = int(date.today().year) - anno_nascita
#age = int(strftime("%Y")) - anno_nascita

# colors

# output

print("="*60)
if age <= 11:
    print("La tua categoria è ESORDIENTI B.")
elif age >= 12 and age <= 13:
    print("La tua categoria è ESORDIENTI A.")
elif age >= 14 and age <= 16:
    print("La tua categoria è RAGAZZI.")
elif age >= 17 and age <= 18:
    print("La tua categoria è JUNIORES.")
elif age >= 19 and age <= 20:
    print("La tua categoria è CADETTI.")
else:
    print("La tua categoria è SENIORES.")
print("="*60)