"""IMC"""

# data

# input

altezza = float(input("Quanti sei alto? "))
peso = int(input("Quanti pesi? "))

# processing

if altezza >= 2:
    altezza = float(altezza / 100)
else:
    altezza = altezza

imc = peso / (altezza ** 2)

# colors

# output

print("=" * 60)
if imc < 19:
    print("Il tuo IMC è {} e sei SOTTOPESO.".format(round(imc)))
elif imc >= 19 and imc <= 24:
    print("Il tuo IMC è {} ed il tuo peso è NELLA NORMA.".format(round(imc)))
elif imc >= 25 and imc <= 30:
    print("Il tuo IMC è {} ed sei SOVRAPESO.".format(round(imc)))
else:
    print('Il tuo IMC è {} sei nella categoria di OBESITÀ.'.format(round(imc)))
print("=" * 60)
