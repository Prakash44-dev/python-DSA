matrix = [[1,2,3],[4,5,6],[7,8,9]]
n = len(matrix)
# exmx = []
# row=[]

# for k in range(n):
#     row = []
#     for i in range(n-1, -1, -1):
#         j = (n-1) - i
#         row.append(matrix[i][k])
#     exmx.append(row)
# matrix=exmx    

# print(matrix)
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for k in range(n):
    matrix[k].reverse()
print(matrix)    

