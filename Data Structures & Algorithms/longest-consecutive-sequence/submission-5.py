class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        max_seq=1
        for i in range(len(nums)-1):
            seq=1
            for j in range(i,len(nums)-1):
                if nums[j]+1==nums[j+1]:
                    seq+=1
                else:
                    break
                if seq>max_seq:
                    max_seq=seq
        return max_seq