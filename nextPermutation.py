class Solution:
    def nextPermutation(self, nums):
        """
        step1. find the farthest slope in nums and get it's index -> idx
        step2. find the another min peak after the above slope who value between nums[idx+1] and  nums[idx], called min_idx
        step3. swap idx and min_idx
        step4. sort nums[idx+1:]
        st
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 1:
            return
        pos = -1
        for i in range(length - 1):
            if nums[i] < nums[i + 1]:
                pos = i
        if pos != -1:
            min_idx = pos + 1
            for i in range(pos+2, length):
                if nums[pos] < nums[i] < nums[min_idx]:
                    min_idx = i
            # swap
            temp = nums[pos]
            nums[pos] = nums[min_idx]
            nums[min_idx] = temp
        else:
            nums.reverse()
            return
        # sort
        nums[pos+1:]= sorted(nums[pos+1:])

test = [1,3,2]
nextPermutation(test)
print(test)