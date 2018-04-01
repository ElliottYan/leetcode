class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        neg = 0
        if x < 0:
            neg = 1
        x = abs(x)
        tmp = []
        while x != 0:
            b = x % 10
            x = x / 10
            tmp.append(b)

        for ix, b in enumerate(tmp):
            ret += b
            if ix != len(tmp) - 1:
                ret *= 10
        print(ret) 

s = Solution()
s.reverse(120)

