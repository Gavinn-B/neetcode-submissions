class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        copy = []
        used = [False] * len(nums)
        self.backtrack(nums,copy,used)
        return self.res

    def backtrack(self, nums: List[int], copy: List[int], used: List[bool]):
        if len(copy) == len(nums):
            if copy:
                self.res.append(copy[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                copy.append(nums[i])
                used[i] = True
                self.backtrack(nums,copy,used)
                copy.pop()
                used[i] = False