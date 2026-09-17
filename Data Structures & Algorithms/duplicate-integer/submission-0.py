class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count={}
        for n in nums:
            count[n]= 1 + count.get(n,0)
            value = count.get(n,0)
            if value>1:
                return True
        return False