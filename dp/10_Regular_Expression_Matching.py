"""
This can be done recursively or other ways. 
Notice, this is called for entire string

1. recursive
firstly, it should be very simple if there is only '.' symbol.
Secondly, we need to take "*" into account.

special case:
if m and n == 0: match!

match_first: s[0] == p[0] or p[0] == "."  ----> m >0 and n > 0

p[1] == '*' :
next step could be 
1. s[:] and p[2:]   
2. s[1:] and p[:]   ---->   if match_first

2. DP

"""

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        ret = False
        if not m and not n:
            ret = True
        if n > 1 and p[1] == "*":
            ret = self.isMatch(s[:], p[2:])
            if m and n and (s[0] == p[0] or p[0] == '.'):
                ret = ret or self.isMatch(s[1:], p[:]) 

        else:
            if m and n and (s[0] == p[0] or p[0] == '.'):
                ret = self.isMatch(s[1:], p[1:])

        return ret

    def isMatch_dp(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[False,] * (n+1) for i in range(m+1)]
        dp[0][0] = True
        # init
        # if j = 0 and i >0: all false

        for i in range(0, m+1):
            for j in range(1, n+1):
                if j >= 2 and p[j-1] == "*":
                    dp[i][j] = dp[i][j-2]
                    if i >= 1 and (p[j-2] == s[i-1] or p[j-2] == '.'):
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    if i > 0 and j > 0 and (s[i-1] == p[j-1] or p[j-1] == '.'):
                        dp[i][j] = dp[i-1][j-1]
        for i in range(0, m+1):
            print(dp[i])
        return dp[m][n]

s = Solution()
print(s.isMatch_dp("","a*"))