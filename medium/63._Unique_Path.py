"""
first thought:
can use recursive method to solve
as long as there is slightly different in each node of path , it should be counted as unique path.

special cases:
m, n <= 0, m, n == 1
m == 1 & n == 1

---> got good result but exceed the time limit

Modified version:
add a dp matrix with size m * n
Each time test whether this value is in dp matrix, use if it is, or compute that if it's not.

Now only dp version, intialize 0 index to 0 and m == 1 and n == 1 to 1.
then iterate in range(2, m+1) and (2, n+1)
each entry (i,j) is the sum of (i-1, j) and (i, j-1)
"""
class Solution:
    dp = []
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # iniitalization
        if m == 1 and n == 1:
            return 1
        global dp
        dp = [[0,] * (n+1)] * (m+1)
        for i in range(m+1):
            dp[i][0] = 1
        for j in range(n+1):
            dp[0][j] = 1
        return self.path_recursive(m-1, n) + self.path_recursive(m, n-1)
        # return self.path_recursive(m-1, n, dp) + self.path_recursive(m, n-1, dp)

    def path_recursive(self, m, n): #, dp):
        # import pdb
        # pdb.set_trace()
        global dp
        if m <= 0:
            return 0
        if n <= 0:
            return 0
        if m == 1:
            return 1
        if n == 1:
            return 1
        # not right with assigning value
        left = dp[m-1][n] if dp[m-1][n] != -1 else self.path_recursive(m-1, n)#, dp)
        right = dp[m][n-1] if dp[m][n-1] != -1 else self.path_recursive(m, n-1)#, dp)
        if m == 4 and n == 2:
            import pdb
            pdb.set_trace()
            # print(left, right)
        # dp[m-1][n] = left
        # dp[m][n-1] = right
        dp[m][n] = left + right

        return left + right

    # only dp implementation
    def uniquePaths2(self, m, n):
        dp = [[0,] * (n+1)] * (m+1)
        for i in range(m+1):
            dp[i][1] = 1
        for j in range(n+1):
            dp[1][j] = 1

        for i in range(2, m+1):
            for j in range(2, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[m][n]



s = Solution()
print(s.uniquePaths2(4, 4))
# print(dp)