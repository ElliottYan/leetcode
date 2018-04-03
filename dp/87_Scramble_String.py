"""
Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

first thought:
can it be thought as a permutation of s1? No!

second thought:
can we use a tree to represent it? or more general way to do that
simulation?

special case:
if s1 == s2, true or false?
"""
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # import string
        # letters = string.ascii_letters
        # count_map = dict()

        # for i in letters:
        #     count_map[i] = 0

        # for i in range(len(s1)):
        #     count_map[s1[i]] += 1
        #     count_map[s2[i]] -= 1

        # 3D matrix
        dp = dict()
        ret = False
        length = len(s1)
        for k in range(length):
            ret = ret or (self.recursive_(s1, s2, 0, 0, k, dp) and self.recursive_(s1, s2, k, k, length-k, dp))
            ret = ret or (self.recursive_(s1, s2, 0, length-k, k, dp) and self.recursive_(s1, s2, k, 0, length-k, dp))
        return ret

    def recursive_(self, s1, s2, i, j, k, dp):
        if (i, j, k) in dp.keys():
            return dp[(i, j, k)]

        ret = False
        if s1[i:i+k] == s2[j:j+k]:
            ret = True

        else:
            for m in range(1, k):
                ret = ret or (self.recursive_(s1, s2, i, j, m, dp) and self.recursive_(s1, s2, i+m, j+m, k-m, dp))
                ret = ret or (self.recursive_(s1, s2, i, j+k-m, m, dp) and self.recursive_(s1, s2, i+m, j, k-m, dp))
        dp[(i, j, k)] = ret
        return ret 

s = Solution()
print(s.isScramble('abcd', 'acbd'))