class Solution {
    public int climbStairs(int n) {
        int[] dp=new int[n+1];
        int res=memoization(dp,n);
        return res;
    }
    public int memoization(int[] dp, int n){
        if(dp[n]!=0){
            return dp[n];
        }
        if(n<0){
            return 0;
        }
        if(n<3){
            return n;
        }
        dp[n]=memoization(dp,n-1)+memoization(dp,n-2);
        return dp[n];
    }
}
