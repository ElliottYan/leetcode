class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows > 2:
            even_row = numRows
            odd_row = numRows - 2
        elif numRows == 2:
            even_row = numRows
            odd_row = 0
        else:
            return s

        first_row = list(range(0, len(s), even_row + odd_row))
        # print(first_row)
        first_row = [s[index] for index in first_row]
        if numRows >=2:
            last_row = list(range(even_row-1, len(s), even_row + odd_row))
            # print(last_row)
            last_row = [s[index] for index in last_row]

        else:
            last_row = []

        tmp = []
        if odd_row:
            # compute middle results
            for j in range(1, odd_row+1):
                column = 0
                odd = 0
                # initialization
                k = 0
                while k < len(s):
                    # if k satisfied this situation
                    if odd == 0:
                        k = column * (even_row + odd_row) + j
                    else:
                        k = column * (even_row + odd_row) - j
                    odd = 1 - odd
                    column += odd
                    if k >= len(s):
                        break
                    tmp.append(s[k])
            # cut off start symble
            print(tmp)
        # print(first_row + tmp + last_row)
        print(len(first_row))
        print(len(tmp))
        print(len(last_row))
        return "".join(first_row + tmp + last_row)


s = Solution()
print(s.convert("ABC", 2))
