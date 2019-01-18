class Solution:
    def threeSumClosest(self, nums, target):
        """
        Problem Description:
            Given an array nums of n integers and an integer target,
            find three integers in nums such that the sum is closest to target.
            Return the sum of the three integers.
            You may assume that each input would have exactly one solution.
        Idea:
            1. Sort the array first: O(n log n)
            2. for each i, find pair (j,k) in range (i+1, length -1), make sure j < k
                3. if nums[i] + nums[j] + nums[k] > target, in order to closest to target, decrease k
                4. if nums[i] + nums[j] + nums[k] < target, in order to closest to target, increase j
                5. if nums[i] + nums[j] + nums[k] = target, directly return target
            6. during 3,4,5 update the min distance

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        nums.sort()
        res = 0
        min_dis = float('inf')
        for i in range(0, length - 2):
            j, k = i+1, length -1
            while j < k:
                candidate = nums[i] + nums[j] + nums[k] - target
                abs_candidate = abs(candidate)
                if abs_candidate < min_dis:
                    min_dis = abs_candidate
                    res = candidate + target
                if candidate > 0:        # 过大，需要变小
                    k -= 1 
                elif candidate < 0:    # 过小，需要变大
                    j += 1
                else:
                    return target
        return res



