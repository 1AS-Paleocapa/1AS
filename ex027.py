name = str(input("Digita il tuo COGNOME / NOME: ")).strip().title()
n1 = name.split()
print("Il tuo cognome è {}.".format(n1[0]))
print("Il tuo nome è {}.".format(n1[len(n1)-1]))
