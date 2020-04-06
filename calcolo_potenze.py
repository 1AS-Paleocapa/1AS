"""Calcolo potenze"""

# input

n = int(input("Digita un mumero: "))

# elaborazione

n2 = n ** 2
n3 = n ** 3
n4 = n ** 4
n5 = n ** 5
n6 = n ** 6
n7 = n ** 7
n8 = n ** 8
n9 = n ** 9
n10 = n ** 10
n100 = n ** 100
n1000 = n ** 1000

# colors

colors = {"clear": "\33[m",
          "start": "\33[1;30;31m"}

# output

print("{}".format(colors["start"]))
print("=" * 40)
print("{} elevato a 2 = {}" .format(n, n2))
print("{} elevato a 3 = {}" .format(n, n3))
print("{} elevato a 4 = {}" .format(n, n4))
print("{} elevato a 5 = {}" .format(n, n5))
print("{} elevato a 6 = {}" .format(n, n6))
print("{} elevato a 7 = {}" .format(n, n7))
print("{} elevato a 8 = {}" .format(n, n8))
print("{} elevato a 9 = {}" .format(n, n9))
print("{} elevato a 10 = {}" .format(n, n10))
print("{} elevato a 100 = {}" .format(n, n100))
print("{} elevato a 1000 = {}" .format(n, n1000))
print("=" * 40)
print("{}".format(colors["start"]))
