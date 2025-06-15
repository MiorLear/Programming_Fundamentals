n = int(input("Matrix size: "))

matrix = []

for i in range(n):
    line = input("Row " + str(i+1) + ": ")
    parts = line.split(",")
    row = []
    for p in parts:
        row.append(int(p))
    matrix.append(row)

symmetric = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False

if symmetric:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
