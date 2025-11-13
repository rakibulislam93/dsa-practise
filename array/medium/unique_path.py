
# find unique path for reach start to end.... time complexity O(2^(m+n)) very slow.
m = 3
n = 3
i,j =0,0
dp = [[-1 for _ in range(n)] for _ in range(m)]
def findUniquePath(m,n,i,j):
    if i==m-1 and j==n-1: return 1
    if i>=m or j>=n: return 0

    # use dynamic memoization
    if dp[i][j] != -1: return dp[i][j]

    dp[i][j] = findUniquePath(m,n,i+1,j) + findUniquePath(m,n,i,j+1)
    return dp[i][j]


print(findUniquePath(m,n,i,j))
print(dp)

# class Solution {
# public:
#     int uniquePaths(int m, int n) {
#         int total_step = m + n -2;
#         int down_step = m-1;

#         long long int ans = 1;

#         for(int i=1; i<=down_step; i++){
#             ans = ans*( total_step - down_step + i) / i;
#         }
#         return ans;
#     }
# };