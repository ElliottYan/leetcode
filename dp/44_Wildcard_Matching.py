"""
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a")  false
isMatch("aa","aa")  true
isMatch("aaa","aa")  false
isMatch("aa", "*")  true
isMatch("aa", "a*")  true
isMatch("ab", "?*")  true
isMatch("aab", "c*a*b")  false


Solution:
of course dp again, but this time with different recursion.


"""
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = dict()
        ret = self.isMatch_recursive(s, p, 0, 0, dp)
        print(dp)
        return ret

    def isMatch_recursive(self, s, p, i, j, dp):
        m = len(s)
        n = len(p)
        if (i, j) in dp.keys():
            return dp[(i,j)]
        ret = False
        if not n and m:
            ret = False
        if not n and not m:
            ret = True
        if m - i > 0 and n - j > 0 :    
            if (s[i] == p[j] or p[j] == "?"):
                ret = self.isMatch_recursive(s, p, i+1, j+1, dp)
            if p[j] == '*':
                ret = self.isMatch_recursive(s, p, i, j+1, dp) or self.isMatch_recursive(s, p, i+1, j, dp)
        dp[(i,j)] = ret
        return ret

    def isMatch1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        if not n and m:
            return False
        if not n and not m:
            return True
        import pdb
        pdb.set_trace()
        if m > 0 and n > 0 and (s[0] == p[0] or p[0] == "?"):
            return self.isMatch1(s[1:], p[1:])
        if n>0 and p[0] == '*':
            if n == 1:
                return True
            return self.isMatch1(s[:], p[1:]) or self.isMatch1(s[1:], p[:])
        return False


s = Solution()
print(s.isMatch('aa', '*'))
print(s.isMatch("zacabz","*a?b*"))