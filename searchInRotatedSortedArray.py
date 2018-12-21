class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the pivot, binary search 
        x = self.find_pivot(nums)
        print(x)
        if x == 0:
            return self.part_binary_search(0,len(nums)-1,nums,target)

        if nums[0] < target:
            return self.part_binary_search(0,x-1,nums,target)
        elif nums[0] == target:
            return 0
        else:
            return self.part_binary_search(x,len(nums)-1, nums, target)

    def part_binary_search(self,left, right, nums, target):
        if left == right:
            if target == nums[left]:
                return left
            else:
                return -1
        mid = int((left + right) / 2)
        if nums[mid] > target:
            return self.part_binary_search(left, mid, nums, target)
        elif nums[mid] < target:
            return self.part_binary_search(mid + 1, right, nums, target)
        else:
            return mid
    @staticmethod
    def find_pivot(nums):
        if nums[0]<=nums[len(nums)-1]:
            return 0
        def binary_search(left, right, nums):
            if left == right or left + 1 == right:
                return right
            mid = int((left + right) / 2)
            if nums[mid] >= nums[left]:
                return binary_search(mid, right, nums)
            return binary_search(left, mid, nums)
        return binary_search(0, len(nums)- 1, nums)




s= Solution()
print(s.search([1,3], 3))