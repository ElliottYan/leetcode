"""
first thought:
use a dp 2 D matrix, which its index (i,j) represents the longest valid parentheses start from i and end at j.

Sol 1
second thought:
use two stack to represent which is not matched and which stores the count start from this
we need a special token the record the length start from 0
every time a new match is given, we simply add 2 to the current count stack
add each time the count stack is poped out, we add it to the previuos count stack item

Sol 2
dp solution
longest[i] saves the longest length end at i
"""
class Solution:
    # sol 1
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # store the parentheses
        stack_a = ['<s>',]
        # store the count
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

    # sol 2: dp solution
    def longestVaildParentheses2(self, s):
        longest = [0]
        ret = 0

        for i, c in enumerate(s):
            if i == 0:
                continue
            # in this way, it couldn't be a valid ending
            if c == '(':
                longest.append(0) 
            else:
                # initialization helps
                print(i - longest[i-1] - 1)
                print(i)
                if i - longest[i-1] - 1 >= 0 and s[i - longest[i-1] - 1] == '(':
                    tmp = longest[i - longest[i-1] - 2] if i - longest[i-1] - 2 > 0 else 0
                    print(tmp)
                    longest.append(longest[i-1] + 2 + tmp)
                    if ret < longest[i]:
                        ret = longest[i]
                else:
                    longest.append(0)
        print(longest)
        return ret
        
s = Solution()
str = input()
print(s.longestVaildParentheses2(str))