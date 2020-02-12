class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1

        i, j = m - 1, n - 1
        index = m + n - 1

        while i >= 0 or j >= 0:
            if j >= 0 and (i < 0 or (i >= 0 and nums1[i] < nums2[j])):
                nums1[index] = nums2[j]
                j -= 1
            else:
                nums1[index] = nums1[i]
                i -= 1
            index -= 1

        return nums1