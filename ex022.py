name = str(input("COGNOME / NOME: ").strip())
print("-" * 80)
print("Il tuo cognome/nome è: {}".format(name.title()))
print("Il tuo cognome/nome tutto in maiuscolo è: {}".format(name.upper()))
print("Il tuo cognome/nome tutto in minuscolo è: {}".format(name.lower()))
print("Il tuo cognome/nome ha {} lettere.".format(len(name) - name.count(" ")))
print("Il tuo cognome ha {} lettere. ".format(name.find(" ")))
print("-" * 80)
name_div = name.split()
print("Il tuo cognome è {} ed ha {} lettere.".format(name_div[0], len(name_div[0])))
print("-" * 80)
