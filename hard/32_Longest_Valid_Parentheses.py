"""
first thought:
use a dp 2 D matrix, which its index (i,j) represents the longest valid parentheses start from i and end at j.

second thought:
use two stack to represent which is not matched and which stores the count start from this
we need a special token the record the length start from 0
"""
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # store the parentheses
        stack_a = ['<s>',]
        # store the index
        stack_b = [0,]

        ret = 0
        if not s:
            return ret

        # also we need a pointer to point the last one of stack
        k = 0
        for i in range(len(s)):
            # in case the stack is empty
            if stack_a[-1] != '(' or s[i] != ')':
                stack_a.append(s[i])
                stack_b.append(0)
                k += 1

            else:
                # count length
                stack_b[k] += 2
                if stack_b[k] > ret:
                    ret = stack_b[k]
                # pop out both
                stack_b[k-1] += stack_b[k]
                stack_a = stack_a[:-1]
                stack_b = stack_b[:-1]
                k -= 1

            print("round %d"%i)
            print(stack_a)
            print(stack_b)
        ret = max([ret, ] + stack_b)
        return ret

        
s = Solution()
str = input()
print(s.longestValidParentheses(str))