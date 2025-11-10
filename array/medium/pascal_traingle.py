
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

n = 5
result = []
for i in range(n):
    row = [1]*(i+1)
    for j in range(1,i):
        row[j] = result[i-1][j-1] + result[i-1][j]

    result.append(row)


print(result)