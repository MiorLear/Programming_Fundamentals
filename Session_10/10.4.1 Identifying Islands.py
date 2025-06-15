n = int(input("Rows: "))
m = int(input("Cols: "))

grid = []

for i in range(n):
    line = input("Row " + str(i + 1) + ": ")
    parts = line.split(",")
    row = []
    for p in parts:
        row.append(int(p))
    grid.append(row)

def visit(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return
    if grid[i][j] != 1:
        return
    grid[i][j] = -1
    visit(i+1, j)
    visit(i-1, j)
    visit(i, j+1)
    visit(i, j-1)

count = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            visit(i, j)
            count += 1

print(count)
