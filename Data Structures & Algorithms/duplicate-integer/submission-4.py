class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for num in nums:
            count[num] = count.get(num,0) + 1
            if count[num] > 1:
                return True
        return False