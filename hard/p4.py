class Solution:
    # Alg 1:
    # recursive: with changing the problem to find Nth number.
    def find_Nth_number(self, nums1, nums2, target):
        len1 = len(nums1)
        len2 = len(nums2)

        print(len1, len2, target)
        if len1 == 0:
            return nums2[target - 1]
        if len2 == 0:
            return nums1[target - 1]

        A_mid = nums1[target // 2 - 1] if target // 2 <= len1 else None
        B_mid = nums2[target // 2 - 1] if target // 2 <= len2 else None

        # import pdb
        # pdb.set_trace()
        if B_mid is None:
            return self.find_Nth_number(nums1[target // 2:], nums2, target - target // 2)
        if A_mid is None:
            return self.find_Nth_number(nums1, nums2[target // 2:], target - target // 2)

        if target == 1:
            return min(nums1[0], nums2[0])
            
        if A_mid < B_mid:
            return self.find_Nth_number(nums1[target // 2:], nums2, target - target // 2)
        else:
            return self.find_Nth_number(nums1, nums2[target // 2:], target - target // 2)

    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        odd = length % 2
        target = length // 2
        if length % 2 == 0:
            return (self.find_Nth_number(nums1, nums2, target) + self.find_Nth_number(nums1, nums2, target + 1)) / 2.0
        else:
            return self.find_Nth_number(nums1, nums2, target + 1)


    # Alg 2:
    # divid two arrays into same length with left-part and right-part.
    # use i to compute j, so constraints: len1 <= len2
    # m <= n, i < m ==> j = (m+n+1)/2 - i > (m+n+1)/2 - m >= (2*m+1)/2 - m >= 0    
    # m <= n, i > 0 ==> j = (m+n+1)/2 - i < (m+n+1)/2 <= (2*n+1)/2 <= n
    def findMedianSortedArrays(self, nums1, nums2):
         """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        # exchange
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1

        imin, imax = 0, len1

        while imin <= imax:
            mid = (imin + imax) / 2 
            i = mid 
            j = (len1 + len2 + 2) / 2 - i

            # each time, we only update the boundary once.
            if i < len1 and B[j-1] > A[i]:
                imin = i + 1

            elif i > 0 and B[j] > A[i-1]:
                imax = i - 1

            else:
                # i is perfect
                # in this case, we need to consider the edge situation
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])



                if i == len1:
                    min_of_right = B[j]
                elif j == len2:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                if (len1 + len2) % 2 == 1:
                    return min_of_right

                else:
                    return (min_of_right + max_of_left) / 2.0

s = Solution()
print(s.findMedianSortedArrays([4], [1,2,3,5,6]))