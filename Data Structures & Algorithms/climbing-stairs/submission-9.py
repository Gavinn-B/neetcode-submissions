class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        one = 1
        two = 2
        for i in range(2,n):
            res = one + two
            one = two
            two = res
        return res