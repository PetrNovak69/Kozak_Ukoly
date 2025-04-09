obchodnici = ["Alice", "Bob", "Cyril", "Denisa", "Eva"]

trzby = [
    [1200, 1350, 1100, 1600, 1800, 1750, 1900],  # Alice
    [1050, 950, 1200, 1100, 1050, 1350, 1300],   # Bob
    [1300, 1450, 1600, 1700, 1750, 1800, 1650],  # Cyril
    [1100, 950, 800, 950, 1000, 1100, 900],      # Denisa
    [1280, 1250, 1350, 1400, 1450, 1500, 1550]   # Eva
]

tydenni_trzby = []
for obchodnik, dny in zip(obchodnici, trzby):
    soucet = sum(dny)
    tydenni_trzby.append((obchodnik, soucet))

print("Tydenni trzby jednotlivych obchodniku:")
for jmeno, trzba in tydenni_trzby:
    print(f"{jmeno}: {trzba} Kc")

nejlepsi = max(tydenni_trzby, key=lambda x: x[1])

print(f"\nObchodnik s nejvyssi tydenni trzbou je {nejlepsi[0]} s trzbou {nejlepsi[1]} Kc.")
