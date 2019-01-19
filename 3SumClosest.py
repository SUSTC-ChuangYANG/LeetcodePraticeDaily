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
        Core idea:
            Chinese：我认为O（n^2）的核心在于一步步缩小解空间的搜索范围。
                    对于一个固定的i，要使得 sum = nums[i] + nums[j] + nums[k] 离 target 足够近，
                    从一开始的搜索范围 (i=i+1, k=length -1) 开始，
                    如果sum比target大，那么离target更近的解，只有可能出现在 (j,k-1) 的范围内，
                    “任何” 包含 k 的求和, 将会使 sum 比 target 大更多 (因为 j 在增加)，即加剧这种偏移，离 target 更远。因此我们可以将 k 从解空间中移走。
                    同理，如果 sum 比 target 小，那么离 target 更近的解，只有可能出现在 (j+1,k) 的范围内，
                    任何包含 j 的其他解，将会使sum 比 target 小更多，即加剧这种偏移，因此我们可以将j从解空间中移走。
                    通过逐步缩小解空间，我们达到了O(n^2)的复杂度.
            English:
                    I think the core of O (n^2) is gradually narrowing the solution space.
                    For a fixed i, to make "sum = nums[I] + nums[j] + nums[k]" close enough to the target,
                    From the beginning of the search range (i = i + 1, k = length - 1),
                    If sum is larger than target,
                        then the solution that is closer to target is only likely to be within range (j, k - 1),
                        "Any" sum value that contains k(left side including j+1,j+2,j+3...) will make sum much larger than
                        current sum and target.(because j is increasing),
                        which exacerbates the offset and make it further away from target.
                        So we can remove k from our solution space.
                    Similarly,
                    If sum is smaller than target,
                        then a solution that is closer to target is only likely to be within range (j + 1, k),
                        "Any" other solution that contains j(right side including k-1,k-2,k-3...) will make sum much smaller
                        than current sum and target,
                        which exacerbates the offset,
                        so we can remove j from the solution space.

                    Step by step to reduce the solution space, we achieve the complexity of O (n ^ 2).

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



