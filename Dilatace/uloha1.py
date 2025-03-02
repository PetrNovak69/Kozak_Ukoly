# Inicializace image2d
image2d = [[4 - max(abs(i - 4), abs(j - 4)) for j in range(9)] for i in range(9)]

# Výstup matice v jednotlivých řádcích
for row in image2d:
    print(row)
