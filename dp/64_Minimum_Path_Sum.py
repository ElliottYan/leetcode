"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

ANS: of course this problem is dp

in spite of the special case, we can each time iterate and chose right or down path in the former node. (Viterbi?)
makes the dp matrix m + 1 * n + 1 makes it much easier
but here the dp matrix is slightly mismatch with grid matrix

special case:
using this alg, the boundary with makes it not very decent to work with.
problems with deep copy and shalow copy. [0,] is mutable objects, cannot use [0,] * k

"""
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        MAX_VAL = 1000000
        dp = [[0,] * (n+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = MAX_VAL
        for j in range(n+1):
            dp[0][j] = MAX_VAL
        
        dp[0][1] = 0
        print(grid)
        for i in range(1, m+1):
            for j in range(1, n+1):
                # import pdb
                # pdb.set_trace()
                # miss the mismatch of grid and dp before..
                dp[i][j] = grid[i-1][j-1] + (dp[i-1][j] if dp[i-1][j] < dp[i][j-1] else dp[i][j-1])

    
        return dp[m][n]

s = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
s.minPathSum(grid)