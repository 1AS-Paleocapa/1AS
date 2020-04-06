"""nome"""

# input

numero = int(input("Digita un numero intero qualsiasi: "))
scelta = int(input("\n"
                   "[ 1 ] per Binario\n"
                   "[ 2 ] per Ottali \n"
                   "[ 3 ] per Esadecimale\n"
                   "\n"
                   "Digita la tua scelta: "))

# processing

# colors

# output

print("\n" + "=" * 60)
if scelta == 1:
    print("Il numero {} in binario é {}." .format(numero, bin(numero)[2:]))
elif scelta == 2:
    print("Il numero {} in binario é {}." .format(numero, oct(numero)[2:]))
elif scelta == 3:
    print("Il numero {} in binario é {}." .format(numero, hex(numero)[2:].upper()))
else:
    print("Scelta non valida.")
print("=" * 60)
