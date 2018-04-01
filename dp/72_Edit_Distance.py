"""
first thought:
assuming m < n where m is len1 and n is len2
can use a array dp to store the difference for sub-string start at index i 
not that right

second thought:
1. use longest common sub-sequence(LCS) algs:
LCS:
use a 2D matrix where (i,j) indicates the longest common sub-String of two sequences end at i and j.

2. after find the biggest common sequence, we simply decided which part we need not to modify.

Solution:
using dp, (i, j) indicates the min cost for converting word1[:i] -> word2[:j]
each step there is three possible operations(not use one is counted as replace)
and we need to consider the min cost after operations (on word1)
(each operation takes place at i and j)
1. Insert
2. delete
3. replace

special case and initialization:
initialize the value of index i, 0 to be i
the same as 0, j

"""
class Solution:
    def minDistance_trial(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        m = len(word1)
        n = len(word2)
        # here we compute the LCS
        lcs = 0
        # dp is size m + 1 * n + 1
        dp = [[0,] * (n+1) for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                # notice that word1 and word2 are in ordinary length
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if dp[i][j] > lcs:
                    lcs = dp[i][j]
        ret = max(m, n) - lcs
        return ret

    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        # dp is size m + 1 * n + 1
        dp = [[0,] * (n+1) for j in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                print(i,j)
                insert_val = dp[i][j-1] + 1
                del_val = dp[i-1][j] + 1
                replace_val = dp[i-1][j-1] if word1[i-1] == word2[j-1] else dp[i-1][j-1] + 1
                print(insert_val, del_val, replace_val)

                dp[i][j] = min(insert_val, del_val, replace_val)
                print(dp[i][j])
        print(dp)
        return dp[m][n]

s = Solution()
s.minDistance('ab','bc')