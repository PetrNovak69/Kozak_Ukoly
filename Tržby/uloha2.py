obchodnici = ["Alice", "Bob", "Cyril", "Denisa", "Eva"]

trzby = [
    [1200, 1350, 1100, 1600, 1800, 1750, 1900],  # Alice
    [1050, 950, 1200, 1100, 1050, 1350, 1300],   # Bob
    [1300, 1450, 1600, 1700, 1750, 1800, 1650],  # Cyril
    [1100, 950, 800, 950, 1000, 1100, 900],      # Denisa
    [1280, 1250, 1350, 1400, 1450, 1500, 1550]   # Eva
]

pocet_obchodniku = len(obchodnici)
pocet_dnu = len(trzby[0])

prumerne_denni_trzby = []
for den in range(pocet_dnu):
    soucet = sum(trzby[obchodnik][den] for obchodnik in range(pocet_obchodniku))
    prumer = soucet / pocet_obchodniku
    prumerne_denni_trzby.append(prumer)

print("Prumerne denni trzby vsech obchodniku:")
for i, prumer in enumerate(prumerne_denni_trzby):
    print(f"Den {i}: {prumer:.2f} Kc")

soucty_dnu = [sum(trzby[obchodnik][den] for obchodnik in range(pocet_obchodniku)) for den in range(pocet_dnu)]
index_max_den = soucty_dnu.index(max(soucty_dnu))

print(f"\nDen s nejvyssim celkovym obratem je den {index_max_den} (0 = pondeli, 6 = nedele).")
