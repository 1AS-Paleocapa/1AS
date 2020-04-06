"""Calcolo della fattibilità di un triangolo"""

# data

# input

s1 = float(input("Digita il primo segmento in cm: "))
s2 = float(input("Digita il primo segmento in cm: "))
s3 = float(input("Digita il primo segmento in cm: "))

# processing

# colors

# output

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Con questi segmenti PUOI formare un triangolo di tipo ", end="")
    if s1 == s2 == s3:
        print("EQUILATERO.")
    elif s1 != s2 != s3 != s1:
        print("SCALENO.")
    else:
        print("ISOSCELE.")
else:
    print("Con questi segmenti NON PUOI puoi formare un triangolo.")
