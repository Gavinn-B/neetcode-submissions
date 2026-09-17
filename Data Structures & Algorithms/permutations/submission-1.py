class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        used = [False] * len(nums)
        self.backtrack([], nums, used)
        return self.res
    
    def backtrack(self, perm: List[int], nums: List[int], used: List[bool]):
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                perm.append(nums[i])
                used[i] = True
                self.backtrack(perm,nums,used)
                perm.pop()
                used[i] = False
        
