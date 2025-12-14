import sys
matrix = [[1,1,1],[1,0,1],[1,1,1]]
n=len(matrix)
for i in range(n):
    for j in range(n):
        if matrix[i][j]==0:
            for k in range(n):
                matrix[k][j]=0
            matrix[i]=[0]*n
            print(matrix)
            sys.exit()
    



