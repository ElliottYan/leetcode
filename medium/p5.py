class Solution:
    # dynamic programming
    def longestPalindrome0(self, s):
        """
        :type s: str
        :rtype: str
        """
        # store bool of i ,j as a palindrome from i to j.
        # cannot use i to indicate the center
        # there exists even cases
        dp = [[False,] * len(s) for i in range(len(s))]

        length = len(s)
        for i in range(length):
            dp[i][i] = True

        max = 0
        ret = s[0]
        for i in range(length -1 , -1 , -1):
            for j in range(i, length):
                # print(i, j)
                dp[i][j] = (j - i < 3 or dp[i+1][j-1]) and s[i] == s[j]
                # print("%d %d %s"%(i ,j ,str(dp[i][j])))
                if dp[i][j]:
                    if j - i + 1 > max:
                        ret = s[i:j+1]
                        max = j - i + 1
        print(ret)
        return ret


    # Manacher
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # make the string to odd length
        tmp = s
        s = "#" + "".join([c + "#" for c in s])
        # print(s)
        i = mx = 0 
        mid = 0
        max = 0
        # length = [0,] * len(s)
        length = []

        for k in range(len(s)):
            import pdb
            # pdb.set_trace()
            if k < mx:
                j = 2 * mid - k
                tmp_l = length[j]
                count = min(tmp_l, mx - i)
                left = k - tmp_l
                right = k + tmp_l 

                for t in range(1, min(left + 1, len(s) - right)):
                    if s[right + t] == s[left - t]:
                        count += 1
                    else:
                        break
                length.append(count)

            else:
                count = 0
                for t in range(1, min(len(s) - k, k + 1)):
                    if s[k + t] == s[k - t]:
                        count += 1
                    else:
                        break
                length.append(count)

            if length[k] > max:
                max = length[k]
                mx = k + length[k]
                mid = k
                ret = s[k - max:k + max + 1]
                # print(k)
                # print(length[k])
                print(ret)

        print(length)
        return ret.replace("#", "")

s = Solution()
print(s.longestPalindrome('babad'))

