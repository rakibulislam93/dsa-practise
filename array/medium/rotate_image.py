
matrix = [[1,2,3],[4,5,6],[7,8,9]]

# output : [[7,4,1],[8,5,2],[9,6,3]]

n = len(matrix)

ans = [ [0 for _ in range(n)] for _ in range(n) ]

for i in range(n):
    for j in range(n):
        ans[j][n-1-i] = matrix[i][j]


print(ans)