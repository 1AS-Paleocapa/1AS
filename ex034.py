stipendio = float(input("Digita l'importo del tuo stipendio atuale: "))
if stipendio >= 1250:
    n = stipendio + ((stipendio/100)*10)
else:
    n = stipendio + ((stipendio/100)*15)
print("*" * 50)
print("Il tuo nuovo stipendio sarà di € {:.2f}.".format(n))
print("*" * 50)
