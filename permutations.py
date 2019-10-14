class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_l = 1
        for i in range(1,len(nums)+1):
            res_l *= i
        res = [[] for i in range(res_l)]
        self.back_tracking(res, nums, 0, res_l)
        print(res)
        return res

    def back_tracking(self, res, nums, start, batch_size):
        length = len(nums)
        if length == 1:
            res[start].append(nums[0])
            return
        batch_size = int(batch_size / length)
        for i, num in enumerate(nums):
            new_start = start+i*batch_size
            self.back_tracking(res, nums[0:i] + nums[i + 1:], start=new_start, batch_size=batch_size)
            for idx in range(new_start, new_start+batch_size):
                res[idx].append(num)

s = Solution()
s.permute([1,2,3,4])
