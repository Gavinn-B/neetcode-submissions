class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newnums=[0]*len(nums)
        for i in range(len(nums)):
            total=1
            for j in range(len(nums)):
                if(i==j):
                    continue
                total*=nums[j]
            newnums[i]=total
        return newnums