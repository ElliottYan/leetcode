class Solution:
    # in this problem ,the * only consider the former one character
    def isMatch1(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # recursive way
        # if there is not star in pattern
        if not pattern: return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        return first_match and isMatch(text[1:], pattern[1:])

    def isMatch2(self, text, pattern):
        # this version consider the stars
        # also a recursive one

        if not pattern: return not text
        # because the star have to take place in the second position
        first_match = bool(text) and pattern[0] in {text[0], '.'}

        # there comes two possibilities
        # we drop the pattern for first match or match recursive ones
        if len(pattern)  >= 2 and pattern[1] == '*':
            return self.isMatch2(text, pattern[2:]) or first_match and self.isMatch2(text[1:], pattern)

        return first_match and self.isMatch2(text[1:], pattern[1:])



sol = Solution()
test = []
result = [sol.isMatch2("aa","a"),
        sol.isMatch2("aa","aa"),
        sol.isMatch2("aaa","aa"),
        sol.isMatch2("aa", "a*"),
        sol.isMatch2("aa", ".*"),
        sol.isMatch2("ab", ".*"),
        sol.isMatch2("aab", "c*a*b")]
print(result)