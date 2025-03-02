image2d = [[4 - max(abs(i - 4), abs(j - 4)) for j in range(9)] for i in range(9)]

print("| " + " | ".join(map(str, range(9))) + " |")
print("|" + " --- |" * 9)

for row in image2d:
    print("| " + " | ".join(map(str, row)) + " |")
