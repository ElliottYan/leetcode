# all input cases: 
# maybe many white spaces at first
# digits, other character + number
# in digit cases: negative / positive / not given, start with several 0, else
# could be bigger or small than INT_MAX, INT_MIN
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str.strip():
            return 0
        str = str.strip()
        ret = 0
        digits = "1234567890"
        sign = "+-"

        negative = 0
        i = 0
        if str[i] in sign:
            # takes in the first character 
            if str[i] == sign[1]:
                negative = 1
            i += 1

        valid = 1
        while i < len(str):
            # if this character is not in digits, return 
            if str[i] not in digits:
                valid = 0
                break
            # execute starts from i + 1
            ret = ret * 10
            # if there is the digits
            ret += int(str[i])
            i += 1

        if negative:
            ret = ret * -1
        # need to compare biggest value and smallest value
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        ret = min(max(INT_MIN, ret), INT_MAX)
        return ret


        