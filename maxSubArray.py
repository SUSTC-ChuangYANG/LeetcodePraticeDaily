

def maxSubArray(nums, algor="dp"):
    """
    :param nums: original number list
    :return: the contiguous sub_array's largest sum.
    """

    # O(n^2)
    if algor == "square":
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]

        max_value = -float('inf')
        for i in range(length):
            sum = nums[i]
            max_value = max(sum, max_value)
            for j in range(i + 1, length):
                sum += nums[j]
                max_value = max(sum, max_value)
        return max_value

    if algor == "fast":
        # use line chart to describe
        if not nums:
            return 0
        max_value = -float('inf')
        seg_sum = 0
        for num in nums:
            if seg_sum + num < 0:
                max_value = max(num, max_value)
                seg_sum = 0
            else:
                seg_sum += num
                max_value = max(seg_sum, max_value)

        return max_value

    if algor == 'divide_conquer':
        length = len(nums)
        if length == 1:
            return nums[0]
        if not nums:
            return 0
        left = self.maxSubArray(nums[0:int(length / 2)], algor='divide_conquer')
        right = self.maxSubArray(nums[int(length / 2):], algor='divide_conquer')
        max_right = -float('inf')
        sum = 0
        for i in range(int(length / 2), length):
            sum += nums[i]
            max_right = max(sum, max_right)

        i = int(length / 2) - 1
        max_left = -float('inf')
        sum = 0
        while i >= 0:
            sum += nums[i]
            max_left = max(sum, max_left)
            i -= 1
        return max(left, right, max_left + max_right)

    # O(n)






x = maxSubArray([-2,1,-3,4,-1,2,1,-5,4],algor="fast")
print(x)
ll = [1,2]
print(ll[2:2])