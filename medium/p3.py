class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # queue & map

        myqueue = []
        max_len = 0
        occured = set()

        for i in range(len(s)):
            c = s[i]
            # always put c
            myqueue.append(c)
            if c not in occured:
                occured.add(c)
            else:
                # indicate the head of queue
                head = myqueue[0]
                i = 1
                while(head != c):
                    occured.remove(head)
                    # dequeue operation
                    head = myqueue[i]
                    i += 1
                myqueue = myqueue[i:]
                # if head == c, we don't need to remove c and add c
            assert len(myqueue) == len(occured)
            if len(occured) > max_len:
                max_len = len(occured)

        return max_len


