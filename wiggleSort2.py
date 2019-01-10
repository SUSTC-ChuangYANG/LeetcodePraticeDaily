
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        self.findKthLargest(nums, int(length/2))
        if length%2:
            max_i = int((length+1)/2)
        else:
            max_i = int(length / 2)
        i = 0
        temp_i = nums[0:max_i][::-1]
        temp_j = nums[max_i:]
        x = 0
        while i < length:
            nums[i] = temp_i[x]
            i += 2
            x += 1
        if length%2:
            j = length - 2

        else:
            j = length - 1
        x = 0
        while j >= 0:
            nums[j] = temp_j[x]
            j -= 2
            x += 1
        return nums







    def findKthLargest(self,nums,k):
        import random
        left, right = 0, len(nums)-1
        while True:
            pivot = nums[random.randint(left, right)]
            sm_len, eq_len, bg_len = self.three_way_partition(nums,pivot,left,right)
            if bg_len >= k:
                left = right - bg_len + 1
            elif bg_len + eq_len >= k:
                return nums[left+sm_len]
            else:
                k -= (eq_len+bg_len)
                right = left + sm_len -1


    def three_way_partition(self, nums, pivot, left, right):
        """
        see BasicAlgorithms/thereWayPartition.py
        for details.
        :return: the length of three parts
        """
        sp, ep = left, right
        i = left
        while i <= ep:
            if nums[i] > pivot:
                self.swap(i,ep,nums)
                ep -= 1

            elif nums[i] < pivot:
                self.swap(i, sp, nums)
                sp += 1
                i += 1
            else:
                i += 1
        return sp-left, ep-sp+1, right-ep

    @staticmethod
    def swap(a,b, nums):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp


def test_model(nums=[]):
    import random
    """
    :param nums: on default, we do not provide test data, it's an random generated array.
    If you like, you can provide your own
    """
    if not nums:
        for i in range(10):
            nums.append(random.randint(1, 100))
    print("Input:", nums)
    s = Solution()
    print("Result:", s.wiggleSort(nums))


if __name__ == '__main__':
    # test_model([1,53,6,765,3,5456,564,64],2)
    test_model([4,5,5,6])