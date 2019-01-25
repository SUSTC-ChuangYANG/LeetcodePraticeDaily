class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_min = 1
        tmp_max = 1
        res = -float('inf')
        for num in nums:
            a1 = tmp_max * num
            a2 = tmp_min * num
            tmp_max = max(a1, a2, num)
            tmp_min = min(a1, a2, num)
            if tmp_max > res:
                res = tmp_max
        return res






