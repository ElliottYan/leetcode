"""
The sub problem is defined as :
what is the number of ways to climb stairs for total steps i

special case:
n = 1, n = 2
"""

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0,] * (n + 1)
        dp[1] = 1
        if n < 2:
            return 1
        dp[2] = 2

        for i in range(3, n+1):
            one = dp[i-1] 
            two = dp[i-2] 
            dp[i] = one + two
        return dp[n]

s = Solution()
print(s.climbStairs(3))


        