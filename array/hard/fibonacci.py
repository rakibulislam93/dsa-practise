class Solution {
public:
    int dp[35];
    int fib(int n) {
        memset(dp,-1,sizeof(dp));
        if(n==0 || n==1)return n;
        if(dp[n]!= -1)
        {
            return dp[n];
        }
        return dp[n] = fib(n-1)+fib(n-2);
    }
};