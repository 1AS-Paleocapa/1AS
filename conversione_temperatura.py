"""Conversione Temperatura da °C a °F e °K"""

# input

celsius = float(input("Digita la temperatura in gradi Celsius da convertire: "))

# processing

fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

# colors

colors = {"clear": "\33[m",
          "start": "\33[1;30;31m"}

# output

print("{}".format(colors["start"]))
print("=" * 40)
print("Temperatura in gradi Celsius = {} °C\n"
      "Temperatura in gradi Fahrenheit = {:.1f} °F\n"
      "Temperatura in gradi Kelvin = {:.1f} °K" .format(celsius, fahrenheit, kelvin))
print("=" * 40)
print("{}".format(colors["clear"]))
