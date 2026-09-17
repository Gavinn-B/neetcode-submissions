class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = set()
        left = 0
        res = 0

        for right in range(len(s)):

            while s[right] in tracker:
                tracker.remove(s[left])
                left += 1
            
            tracker.add(s[right])
            res = max(res, right - left + 1)
        return res