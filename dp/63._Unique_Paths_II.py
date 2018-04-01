"""
length of obstacleGrid could be 0.
first thought:
use a same matrix dp for accumulating the results, when the obstacle is find in (i,j), the dp[i][j] is set to 0.
special case:
set (0,0) = 1 and this special value cannot be update using left + right, for summing up from range(0,m) and range(0,n)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0 or n == 0:
            return 0
        dp = [[0,] *  n] * m

        # for i in range(m):
        #     dp[i][0] = 1
        # for j in range(n):
        #     dp[0][j] = 1
        dp[0][0] = 1

        # iteration start from 1
        # if the index is smaller than 1
        for i in range(0, m):
            for j in range(0, n):
                # means here is a obstacle
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if i == 0 and j == 0:
                    continue
                else:
                    left = dp[i-1][j] if i > 0 else 0
                    right = dp[i][j-1] if j > 0 else 0
                    dp[i][j] = left + right

        return dp[m-1][n-1]



