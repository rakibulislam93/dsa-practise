
# find unique path for reach start to end.... time complexity O(2^(m+n)) very slow.
m = 3
n = 2
i,j =0,0
def findUniquePath(n,m,i,j):
    if i==n-1 and j==m-1: return 1
    if i>=n or j>=m: return 0
    result = findUniquePath(n,m,i+1,j) + findUniquePath(n,m,i,j+1)
    return result


print(findUniquePath(n,m,i,j))