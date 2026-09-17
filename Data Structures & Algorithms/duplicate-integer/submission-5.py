class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = dict()
        for num in nums:
            if num in count:
                return True
            count[num] = 1
        return False