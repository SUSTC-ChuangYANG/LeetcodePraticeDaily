class Solution:
    def getPermutation(self, n, k):
        """
        1. Problem Definition:
            The set [1,2,3,...,n] contains a total of n! unique permutations(排列).
            By listing and labeling all of the permutations in order,
            we get the following sequence for n = 3:
                                        +------------+
                                        |   "123"    |
                                        |   "132"    |
                                        |   "213"    |
                                        |   "231"    |
                                        |   "312"    |
                                        |   "321"    |
                                        +------------+
            Given n and k, return the kth permutation sequence.
        2. Solution:
            a. performance:
               36 ms, faster than 100.00% of Python3 online submissions for Permutation Sequence.
            b. idea:
               Assuming there are n sorted candidates. we need to find the kth.
               The structure of the n sorted candidates are as follow:
               The size of each block is (n-1)!

                         blockSize = (n-1)!

               No.0     +--------------+
                        |   "1...."    |   1th
                        |   "1...."    |    .
                        |      .       |    .
                        |      .       |    .
                        |   "1...."    |   blockSize th
                        +--------------+
                               +
               No.1     +--------------+
                        |   "2...."    |   blockSize+1 th                          .
                        |   "2...."    |    .
                        |      .       |    .
                        |      .       |    .
                        |   "2...."    |   2*blockSize th
                        +--------------+
                               +
                               .
                               .
               No.m-1   +--------------+   =========================>>
                        |   "m...."    |   (m-1)*blockSize+1 th
                        |   "m...."    |    .
                        |      .       |    .
                        |      .       |    .
                        |   "m...."    |   m*blockSize th
                        +--------------+   =========================>>
                               +
                               .
                               .
               No.n-1   +--------------+
                        |   "n...."    |   (n-1)*blockSize+1 th
                        |   "n...."    |    .
                        |      .       |    .
                        |      .       |    .
                        |   "n...."    |   n*blockSize th
                        +--------------+

                           Figure1

               Now assume the k-th is in the No.m block.
               The internal structure of No.m block is the same as the structure of the above .
               Now the block_size is (n-2)!

                                        blockSize = (n-2)!

                        No.0            +--------------+
                                        |   "m1...."   |
                                        |   "m1...."   |
                                        +--------------+   From 1th --> blockSize th
                                               +
                        No.1            +--------------+
                                        |   "m2...."   |
                                        |   "m2...."   |
                                        +--------------+   From blockSize+1 th --> 2*blockSize th
                                               +
                        No.2            +--------------+
                                        |   "m3...."   |
                                        |   "m3...."   |
                                        +--------------+   From 2*blockSize+1 th --> 3*blockSize th
                                               +
                                               .
                                               .
                        No.m-2          +--------------+
                                        |   "m(m-1)...."
                                        |   "m(m-1)...."
                                        +--------------+   From (m-2)*blockSize+1 th --> (m-1)*blockSize th
                                               +
                        No.m-1          +--------------+
                                        |  "m(m+1)..." |
                                        |  "m(m+1)..." |
                                        +--------------+   From (m-1)*blockSize+1 th --> m*blockSize th
                                               +
                                               .
                                               .
                        No.n-2          +--------------+
                                        |   "mn...."   |
                                        |   "mn...."   |
                                        +--------------+   From (n-2)*blockSize+1 th --> (n-1)*blockSize th

                                        Figure 2


               At start we define "rest_nums" which include all the numbers that are not selected.
                                  rest_nums =[1, 2, 3, .......n]
                                                   --- initial it include all numbers orderly.

               Obviously, Finding the block that k-th belongs to could reduce the search space size to (n-1)!
               Now we calculate
                                        k/(n-1)!   --- (n-1)! is the block_size.
               the integer part of above expression indicate the block Number(i.e., i).
               So we get the first number of the result : rest_nums[i].
               and the remainder part(i.e, r) of above expression indicate the position of(i.e. offset) k in that block.

               Then we set k equal to r, block_size equal to (n-2)!, remove rest_nums[i] from rest_nums.
               again call above procedure,
               then, we get another block Number j.
               At this time, left_nums[j] is the second number of the result.
               Then update k, block_size and remove rest_nums[j] from rest_nums.

               Now, you must have found this is an recursive procedure.

               We again and again do the above procedure until meet the stop condition.
               The stop condition is: we find current k is the end of a block. i.e., r = 0, offset equal to 0
               When meet the stop condition:
                               remove rest_nums[i] from rest_nums.
                               then reverse rest_nums
                               add all num in rest_nums to result.



        :type n: int
        :type k: int
        :rtype: str
        """
        rest_nums = [i for i in range(1, n+1)]
        unit_size = 1
        for i in range(1, n):
            unit_size *= i
        return self.recursive_search(unit_size, k, rest_nums, '')

    def recursive_search(self,unit_size, k, rest_nums, res):
        position, r = int(k / unit_size), k % unit_size
        if r == 0:
            res += str(rest_nums.pop(position-1))
            for num in rest_nums[::-1]:
                res += str(num)
            return res
        # update
        res += str(rest_nums.pop(position))
        unit_size /= len(rest_nums)
        return self.recursive_search(unit_size, r, rest_nums, res)


s= Solution()
print(s.getPermutation(8,720))