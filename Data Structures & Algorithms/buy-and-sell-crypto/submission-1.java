class Solution {
    public int maxProfit(int[] prices) {
        int profit=0;
        for(int i=prices.length-1;i>0;i--){
            for(int j=0;j<i;j++){
                if(prices[i]-prices[j]>profit){
                    profit=prices[i]-prices[j];
                }
            }
        }
        return profit;
    }
}
