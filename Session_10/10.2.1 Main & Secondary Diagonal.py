size = int(input("Matrix size (N): "))

matrix = []

for i in range(size):
    row = input("Row " + str(i + 1) + ": ")
    nums = row.split(",")
    int_nums = []
    for n in nums:
        int_nums.append(int(n))
    matrix.append(int_nums)

main_diag = []
sec_diag = []

for i in range(size):
    main_diag.append(matrix[i][i])
    sec_diag.append(matrix[i][size - i - 1])

print("Main diagonal:", main_diag)
print("Secondary diagonal:", sec_diag)
