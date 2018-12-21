import timeit
class Solution:
    def search(self, nums, target):
        """
        可以想象成一个剪枝的过程，
        有一个潜在的规律， 将一个 RotatedSortedArray 切成两半，
        Example (1)[4,5,6,7,0,1,2,3]
        Example (2)[4,5,6,7,8,0,1,2]
        如果左半部分是有序的，
                    ----- 右半部分有序 (1) [0,1,2,3]
                    ----- 右半部分无序 (2) [8,1,2,3]
                    对于（1）（2） 我们只需判断 target 在不在 [4,5,6,7] 之间，即可确定下一步的搜索范围
                    再次对右半部分求解即可
        如果左半部分是无序的，
                    ----- 右半部分一定是有序的，
                    我们只需判断 target 在不在右半部分即可确定下一步的搜索范围。

        什么时候中止呢？
        搜索范围是 2 的时候就可以停止了。方便还好想 => while (left+1 < right)
        当搜索范围是 3 的时候， 搜索范围会变成 [0,1] 和 [2]
        当搜索范围是 4 的时候， 搜索范围会变成 [0,1] 和 [2,3]
        以上的四种搜索范围， 对与一个target 来说，就是两步操作，完全没必要在递归一次。
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        原始的二分查找会变成：while(left <= right)
        [0,1,2] mid 是 1，
            之后会变成两个单元素
            [0,0]
            => mid = 0
            => 新的范围 [0,-1] 和 [1,0] 两个无法满足 left <= right 规则的东西，然后返回 -1
            [2,2]
            => mid = 2
            => 新的范围 [2,1] 和 [3,2] 两个无法满足 left <= right 规则的东西，然后返回 -1
        原始的二分查找会变成：
        [0,1,2,3] mid 是 1，
            之后会变成
            [0,1]
            => mid = 0
            => 新的范围 [0,-1] 和 [1,1]
            [2,3]
            => mid = 2
            => 新的范围 [2,1] 和 [3,3]
        如此复杂，不如直接在长度为2的时候就返回，然后比较。
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the pivot, then binary search
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1


        left, right = 0, len(nums)-1
        while left + 1 < right:
            print(left, right)
            mid = (left+right) // 2
            # print("left:",left,"right:",right,"middle:",mid)
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[left]:  # 左边有序，右边有序或无序
                # 搜左边的情况
                if nums[left] <= target < nums[mid]: # 搜左边
                    right = mid - 1
                # 搜右边的情况
                else:
                    left = mid + 1
            else:                      # 左边无序， 右边有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        if nums[left] == target:
                return left
        if nums[right] == target:
                return right
        return -1


s= Solution()
print(s.search([4,5,6,7,0,1,2],3))
t = timeit.timeit(stmt="s.search([1,3],3)",setup="from __main__ import Solution; s = Solution()",number=10000000)
print(t)