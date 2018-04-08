"""
Problem set:
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

Solutions:
Noticing that the s1 and s2 itself should stay in its origin order
1. recursive solve whether this could be the result of last i of s1 or last j of s2

2.dp ways:
iterative update the i and j index for which denoting whether sub-string of s1 and s2 forms s3

3. dfs
"""

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1 = len(s1)
        len2 = len(s2)
        if len(s3) != len1 + len2:
            return False

        dp = [[None,] * (len2+1) for i in range(len1+1)]
        dp[0][0] = True
        for i in range(1, len1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, len2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                k = i + j 
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[k-1]) or (dp[i][j-1] and s2[j-1] == s3[k-1])
                # left = dp[i-1][j] and s1[i-1] == s3[k-1]
                # right = dp[i][j-1] and s2[j-1] == s3[k-1]
                print(dp[i][j])
                print('\n')
        for i in range(len1+1):
            print(dp[i])
        return dp[len1][len2]

    # dfs
    def isInterLeave_v2(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        if(m + n != len(s3)) return False;
        invalid = dict()
        return self.dfs(s1, s2, s3, 0, 0, 0, invalid)

    def dfs(self, s1, s2, s3, i, j, k, invalid):
        if k == len(s3):
            return True
        if (i,j) in invalid.keys():
            return False
        ret = i < len(s1) and s1[i] == s3[k] and self.dfs(s1, s2, s3, i+1, j, k+1)
        ret = ret or (j<len(s2) and s2[j] == s3[k] and self.dfs(s1, s2, s3, i, j+1, k+1))
        
        if not ret:
            invalid[(i, j)] = True

        return ret


        
s = Solution()
# print(s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
print(s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
