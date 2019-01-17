"""
Problem Description:
    Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
Idea:
    For any unsorted array nums, we can sort it and get the median.
    Then we can split it into two parts in the middle. As you can image,
    any one of the left part is smaller than the one in right.
    So we can bind one from the left and one from the right,
    obviously, the left one is always no larger than right.(<=)
    But now our requirement is "<" instead of "<=".
    So How?

    |   |
    |   |   |
    |   |   |   |
    |   |   |   |   |
    -------------------------
      |   |
      |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
    As you can see, split the sorted array into two part,
    and combine them from high to low, make the different between two neighbors as big as possible.
    Is A SOLUTION!
    But!
    1. Sort need O(n log n)
    2. Make adjustment and exchange within each parts(except adjust the median's position),
       we still satisfy the "wiggle" attributes.

    This is excellent!
    We just need to split an unsorted array into three parts,
        part "left" is smaller than median,
        part "middle" is equal to the median,
        part "right" is larger than median.
    Cut the semi-sorted array into two parts.
    |   |
    |   |       |
    |   |       |   |
    |   |   |   |   |
    -------------------------
      |       |
      |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |

    Semi-sorted is an O(n) !!!, so we get it.
"""
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length <=1:
            return
        self.findKthLargest(nums, int((length)/2)+1)
        print(nums)
        max_i = (length-1)//2 + 1
        temp_i = nums[0:max_i][::-1]
        temp_j = nums[max_i:][::-1]
        i = 0
        while i < length:
            if i%2 == 0:
                nums[i] = temp_i[i//2]
            else:
                nums[i] = temp_j[i//2]
            i += 1
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
    test_model([4,5,10,8,7])