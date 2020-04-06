print("-=-" * 14)
print("Calcolo della fattibilità di un triangolo: ")
print("-=-" * 14)
s1 = float(input("Digita il primo segmento in cm: "))
s2 = float(input("Digita il primo segmento in cm: "))
s3 = float(input("Digita il primo segmento in cm: "))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print("Con questi segmenti PUOI formare un triangolo.")
else:
    print("Con questi segmenti NON PUOI puoi formare un triangolo.")
