stipendio = float(input("Digita il tuo stipendio lordo: "))
trattenute = float(input("Digita la percentuale delle trattenute: "))
netto = (stipendio * trattenute) / 100
stipendionetto = stipendio - netto
print("-" * 80)
print("Tenendo conto del {:.0f}% di trattenute, il tuo stipendio netto sarà di {:.2f}€.".format(trattenute, stipendionetto))
print("-" * 80)