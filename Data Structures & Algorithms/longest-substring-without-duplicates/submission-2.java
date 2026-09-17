class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        HashMap<Character, Integer> tracker = new HashMap<>();
        char[] chars = s.toCharArray();
        for(int i = 0; i < chars.length; i++){
            tracker.clear();
            int count = 0;
            for(int j = i; j < chars.length; j++){
                tracker.put(chars[j], tracker.getOrDefault(chars[j], 0) + 1);
                if(tracker.get(chars[j]) > 1){
                    break;
                }
                count++;
            }
            res = Math.max(res,count);
        }

        return res;
    }
}
