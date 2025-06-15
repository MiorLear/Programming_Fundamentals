n = int(input("Rows: "))
m = int(input("Cols: "))

matrix = []

for i in range(n):
    row = input("Row " + str(i + 1) + ": ")
    items = row.split(",")
    temp = []
    for it in items:
        temp.append(int(it))
    matrix.append(temp)

result = []

for i in range(n):
    line = []
    for j in range(m):
        count = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if x >= 0 and x < n and y >= 0 and y < m:
                    if not (x == i and y == j):
                        if matrix[x][y] == 1:
                            count += 1
        line.append(count)
    result.append(line)

for r in result:
    print(r)
