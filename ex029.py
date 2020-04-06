v = int(input("Digita la velocità: "))
if v <= 80:
    print("La tua velocità è di {} km/h, complimenti, sei nei limiti di velocità." .format(v))
else:
    m = (v-80)*7
    print("La tua velocità è di {} km/h. Multa di {:.2f}€." .format(v, m))
