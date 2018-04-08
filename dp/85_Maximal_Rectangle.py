"""
we can use the upper-left to low-right to indicate the matrix.
The store value is whether it's full of ones.

Second thought:
thinking the dp[i,j] means that the maximum area of full 1 sub matrix ended at (i, j)
by which we can derive the recurrance.

dp[(i,j)] = dp[(i, j-1)] + dp[(i-1, j)] - dp[(i-1, j-1)] + 1
This proves wrong....

Solution:
use the idea for Largest Rectangle in Histogram (Prob. 84)
histogram array stores the 
 
special case:
consider the row length or column length to be 0 or 1
"""
class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if not m:
            return 0
        n = len(matrix[0])
        if not n:
            return 0

        max_val = 0
        histogram = [[0,] * (n+1) for j in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    histogram[i][j] = histogram[i-1][j] + 1
                # print(matrix[i-1][j-1])
                # print(histogram[i-1][j])
        # Then calculate for each row
        for i in range(1, m+1):
            row = histogram[i][:]
            row.append(-1)
            stack = [-1,]
            for j in range(1, n+2):
                # if j == n+1:
                    # import pdb
                    # pdb.set_trace()
                if row[j] >= stack[-1]:
                    stack.append(row[j])
                else:
                    count = 0
                    # while row[j-1] < stack[-(count+1)]:
                        # count += 1
                        # area = count * stack[-(count+1)]
                    for k in range(len(stack)-1, -1, -1):
                        if stack[k] <= row[j]:
                            break
                        count += 1
                        area = count * stack[k]
                        if max_val < area:
                            max_val = area
                    stack = stack[:-count] + [row[j]] * (count+1)
                print(stack)

        print(max_val)      
        # for i in range(m):
            # print(stack[i])
        for i in range(m+1):
            print(histogram[i])
        return max_val

s = Solution()
s.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])