from random import randint
from time import sleep
pc = randint(0, 5)
print("-=-"*20)
print("Sto pensando in un numero da 0 a 5...")
print("-=-"*20)
sleep(3)
user = int(input("In quale numero ho pensato, prova a indovinarlo: "))
print("-=-"*20)
if user == pc:
    print("Hai vinto, complimenti !!!")
else:
    print("Hai perso, ho pensato al numero {} ritenta." .format(pc))
print("-=-"*20)
