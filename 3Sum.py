class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        length = len(nums)
        # handle special cases
        # case1
        if length < 3:
            return []
        nums.sort()
        # case2
        if nums[length - 1] < 0:
            return []

        for i in range(0, length - 2):
            if nums[i] > 0:
                break
            if nums[i] == nums[i - 1] and i >= 1:
                continue
            j, k = i + 1, length - 1
            while k > j:
                sum = nums[j] + nums[k] + nums[i]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                if sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    if j >= i + 2 and k <= length - 2:
                        if nums[j] == nums[j - 1] or nums[k] == nums[k + 1]:
                            res.pop(len(res) - 1)
                    k -= 1
                    j += 1

        return res


def main():
    s =Solution()
    nums = [0,-4,-1,-4,-2,-3,2]
    print(s.threeSum(nums=nums))
if __name__ == "__main__":
    main()