mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 23] ]
target = 13
m = len(mat)
n = len(mat[0])
res = False
req = 0
# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if mat[i][j] == target :
#             res = True
            
#             break
for i in range(m):
    if mat[i][0] == target or mat[i][n-1] == target :
        res = True

    elif mat[i][0]<target and mat[i][n-1]>target:
        req = i
        break

if target in mat[i] :
    res = True
             
print(res)                