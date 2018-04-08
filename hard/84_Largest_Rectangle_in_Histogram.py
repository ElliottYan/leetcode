"""
Solution 1:
keep a stack, which is allways increasing.
each time it comes to a lower number x, compute area based on now idx and count, set all bigger int to x and push them back to stack s

Solution 2:
dp solution
keep a most left and most right dp array to keep the left and right bound for each point 

trick point:
we cannot compare each point with all its left or right points. 
We iteratively choose current point that need to compare. Each time cur pointer is point to a smaller number.
E.g. for left case:
            cur = i - 1
            while cur >= 0 and heights[cur] > heights[i]:
                left[i] = left[cur]
                cur = left[cur] - 1
"""
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        if not heights:
            return 0
        stack = [0]
        heights.append(0)
        print(heights)
        max_area = 0
        for i in range(len(heights)):
            print(stack)
            if heights[i] >= stack[-1]:
                stack.append(heights[i])
            else:
                k = len(stack) - 1
                count = 0
                while heights[i] < stack[k] and k >= 0:
                    count += 1
                    # print(count)
                    # print(stack[k])
                    area = count * stack[k]
                    if max_area < area:
                        max_area = area
                    k -= 1
                    # print(max_area)
                stack = stack[:-count] + [heights[i],] * (count + 1)
                # print((count + 1) * stack[k])
                # if max_area < (count + 1) * heights[i]:
                    # max_area = (count + 1) * heights[i]
        return max_area

    def largestRectangleArea_dp(self, heights):
        n = len(heights)
        if n == 0:
            return 0
        left = [i for i in range(n)]

        right = [i+1 for i in range(n)]
        print(heights)
        for i in range(1, n):
            # indicates the next value to compare
            cur = i - 1
            while cur >= 0 and heights[cur] > heights[i]:
                left[i] = left[cur]
                cur = left[cur] - 1

        for j in range(n-1, -1, -1):
            cur = j + 1
            while cur < n and heights[cur] > heights[j]:
                right[j] = right[cur]
                cur = right[cur]

        print(left)
        print(right)
        max_val = 0
        for i in range(n):
            tmp = heights[i] * (right[i] - left[i])
            if max_val < tmp:
                max_val = tmp

        return max_val

s = Solution()
print(s.largestRectangleArea_dp([2,1,5,6,2,3]))