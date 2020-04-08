from math import sqrt
from time import sleep

while True:

    print("""
        CALCOLATRICE IN PYTHON
        Creata da Martinelli E.
        
        Operazioni posibili:
        
        [ + ] ADIZIONE
        [ - ] SOTTRAZIONE
        [ X ] MOLTIPLICAZIONE
        [ / ] DIVISIONE
        [ ^ ] ELEVAMENTO A POTENZA
        [ Q ] RADICE QUADRA
        
        Scrivi EXIT per uscire...
        """)

    operazione = str(input("Effetua la tua scelta: ").upper().strip())

    if operazione == "+":
        print("=" * 60)
        n1 = float(input("Digita il primo numero: "))
        n2 = float(input("Digita il secondo numero: "))
        print("=" * 60)
        print("La somma di {} e {} è uguale a {}." .format(n1, n2, n1 + n2))
        print("=" * 60)

    elif operazione == "-":
        print("=" * 60)
        n1 = float(input("Digita il primo numero: "))
        n2 = float(input("Digita il secondo numero: "))
        print("=" * 60)
        print("La sottrazione di {} da {} è uguale a {}." .format(n2, n1, n1 - n2))
        print("=" * 60)

    elif operazione == "X":
        print("=" * 60)
        n1 = float(input("Digita il primo numero: "))
        n2 = float(input("Digita il secondo numero: "))
        print("=" * 60)
        print("La moltiplicazione tra {} e {} è uguale a {}." .format(n1, n2, n1 * n2))
        print("=" * 60)

    elif operazione == "/":
        print("=" * 60)
        n1 = float(input("Digita il primo numero: "))
        n2 = float(input("Digita il secondo numero: "))
        print("=" * 60)
        print("{} diviso {} è uguale a {} con il resto di {}." .format(n1, n2, n1 / n2, n1 // n2))
        print("=" * 60)

    elif operazione == "^":
        print("=" * 60)
        n1 = float(input("Digita la base: "))
        n2 = float(input("Digita lo esponente: "))
        print("=" * 60)
        print("{} elevato a {} è uguale a {}." .format(n1, n2, n1 ** n2))
        print("=" * 60)

    elif operazione == "Q":
        print("=" * 60)
        n1 = float(input("Digita il numero del quale vuoi conoscere  la radice quadrata: "))
        print("=" * 60)
        print("La radice quadrata di {} è uguale a {}." .format(n1, sqrt(n1)))
        print("=" * 60)

    elif operazione == "EXIT":
        print("=" * 60)
        print("Il programma verrà chiuso a breve...")
        print("=" * 60)
        sleep(2)
        break
    else:
        print("=" * 60)
        print("Scelta non valida...")
        print("=" * 60)

    loop = str(input("\nVuoi fare un'altro calcolo? [S/N]: ").strip().upper())

    if loop == "S":
        print("=" * 60)
        print("A breve tornerai al menu principale.")
        print("=" * 60)
        sleep(2)
        continue
    if loop == "N":
        print("=" * 60)
        print("Il programma verrà chiuso a breve 1...")
        print("=" * 60)
        sleep(2)
        break
    else:
        print("=" * 60)
        print("Scelta non valida...")
        print("=" * 60)
        continue