matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

srow = 0
scol = 0
erow = len(matrix) - 1
ecol = len(matrix[0]) - 1

res = []

while srow <= erow and scol <= ecol:

    # left → right
    for i in range(scol, ecol + 1):
        res.append(matrix[srow][i])
    srow += 1

    # top → bottom
    for i in range(srow, erow + 1):
        res.append(matrix[i][ecol])
    ecol -= 1

    # right → left
    if srow <= erow:
        for i in range(ecol, scol - 1, -1):
            res.append(matrix[erow][i])
        erow -= 1

    # bottom → top
    if scol <= ecol:
        for i in range(erow, srow - 1, -1):
            res.append(matrix[i][scol])
        scol += 1

print(res)