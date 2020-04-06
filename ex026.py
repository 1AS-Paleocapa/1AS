frase = str(input("Digita una frase: ")).strip().upper()

print("-" * 80)
print("La lettera A compare {} volte nella tua frase.".format(frase.count("A")))
print("Per la prima volta compare nella posizione n° {}.".format(frase.find("A")+1))
print("E per l'ultima volta nella posizione n° {}.".format(frase.rfind("A")+1))
print("-" * 80)
