"""
check for palindrome numbers
without using extra space
maybe hold a start and end pointer 
need to deal with odd or even cases
and the number could be negative

cannot got x to string, usng extrac space
we need to have two pointers
rev_half means we take the second half
x when we have the first half
"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # consider the case x is negative
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False

        rev_half = 0

        while x > rev_half:
            rev_half = rev_half * 10 + x % 10
            x = int(x / 10)

        return (x == rev_half or x == int(rev_half / 10))




s = Solution()
print(s.isPalindrome(121))