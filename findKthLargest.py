class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return self.random_method(nums,k)

    """
    heap method
    Idea: 
        build a k-size min-heap, 
        for loop each left nums, 
            if bigger than heap head,
                pop out head and push the bigger num
        In the end, the head of heap is the target we search.
    Time Complexity: 
        heapq is binary heap, with O(log n) push and O(log n) pop, and O(n) build
        so here is O(k+(n-k)*log k) 
    Space Complexity:    
        O(k), the cost of store heap
    """
    def heap_method(self,nums,k):
        import heapq
        hp = nums[0:k]
        heapq.heapify(hp)
        for num in nums[k:]:
            if num > hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, num)
        return hp[0]

    """
    Idea: split the array to three part, 
          then narrow down the search region, 
            if big part no less than k, new region is big part
            if big part and equal part no less than k, we get the result
            if big part and equal part smaller than k, new region is small part, and k changed
          on average, reduce half of current region, if you would like to prove use expectation.
    Time Complexity:    
        T(n) = T(n/2) + O(n) on average
        Assume n is the power of 2
        So T(n) = 1 + 2 + 4 + n/4 + n/2 + n = 2n , O(n)
        a1(1-q^n)/1-q = n(1-0.5^log n)/(1-0.5) = 2n(1-(1/2n)) = 2n
    Space Complexity:    
        O(1), because we just use "swap"
    
    """
    def random_method(self,nums,k):
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


def test_model(nums=[], k=1):
    import random
    """
    :param nums: on default, we do not provide test data, it's an random generated array.
    If you like, you can provide your own
    """
    if not nums:
        for i in range(10):
            nums.append(random.randint(1, 100))
    print("Input:", nums)
    print("K:", k)
    s = Solution()
    print("Result:", s.findKthLargest(nums,k))


if __name__ == '__main__':
    # test_model([1,53,6,765,3,5456,564,64],2)
    test_model()
    test_model(k=3)