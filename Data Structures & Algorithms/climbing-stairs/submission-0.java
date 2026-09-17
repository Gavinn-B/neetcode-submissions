class Solution {
    public int climbStairs(int n) {
        if (n<3){
            return n;
        }
        int one=1,two=2,c=3;

        for(int i=3;i<n;i++){
            one=two;
            two=c;
            c=one+two;
        }
        return c;
    }
}
