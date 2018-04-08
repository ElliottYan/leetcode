"""
first thought:
consider search algorithms

Solution 1:


special case:
1. '0'
2. ''
3. '10'
4. start with 0s
5. different partition makes the same result
"""
class Solution:

    # def numDecodings(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     count = 1
    #     dp = dict()
    #     ret = self.search(s, 0, len(s), dp)
    #     print(ret)
    #     return ret

    # def search(self, s, i, j, dp):

    #     if (i,j) in dp.keys():
    #         return dp[((i, j))]
    #     ret = 0
    #     n = j - i
    #     if n > 0 and s[i] == '0':
    #         ret = 0
    #     elif n == 1 and int(s[i:j]) > 0 :
    #         ret = 1
    #     elif n == 2 and int(s[i:j]) <= 26 and int(s[i:j]) > 0:
    #         if int(s[i:j]) == 10:
    #             ret = 1
    #         else:
    #             ret = 2
    #     else:
    #         # for k in range(1, n):
    #         tmp = self.search(s, i, i+1, dp) + self.search(s, k+i, j, dp)
    #             print("in (%d, %d)"%(i, j))
    #             print("k = %d"%k)
    #             print(tmp)
    #             ret += tmp
    #     dp[(i, j)] = ret
    #     return ret

    #     ret = 0
    #     n = j - i
    #     if n == 0:
    #         return True
    #     if n > 1:
    #         if s[i] != '0':
    #             ret += 1 if search(i+1) else 0

    def numDecodings_dp(self, s):
        n = len(s)
        if not n:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if i > 0 and s[i-1] != '0':
                dp[i] += dp[i-1]
            if i > 1 and int(s[i-2:i]) <= 26 and int(s[i-2:i]) >= 10:
                dp[i] += dp[i-2]
        print(dp)
        return dp[n]


s = Solution()
print(s.numDecodings_dp('21'))