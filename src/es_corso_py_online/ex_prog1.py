name = str(input("Tuo nome:"))
year = int(input("Anno di nascita: "))
place = str(input("Luogo di nascita: "))
height = float(input("Altezza (m) : "))
weight = float(input(" Peso (kg): "))
today = int(2025)

print(f" {name}, {today-year} anni, nato a {place} nel {year}, altezza: {height: .2f} m, peso: {weight: .2f} kg")
