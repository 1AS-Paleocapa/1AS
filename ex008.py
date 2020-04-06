m = float(input("Digita un valore in metri: "))
print()
km = m / 1000
hm = m / 100
dam = m / 100
dm = m * 10
cm = m * 100
mm = m * 1000
print("{:.3f} km \n{:.3f} hm \n{:.3f} dam \n{:.0f} m \n{:.0f} dm \n{:.0f} cm \n{:.0f} mm".format(km, hm, dam, m, dm, cm, mm))
