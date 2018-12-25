import timeit
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        ---------------------------------------------------------------------------
        Problem Description: 
        	Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
        Time complexity: O(n^2)
        Recursion formula: T(n) = T(0) * T(n-1) + T(1) * T(n-2) + … + T(n-1) * T(0)
        ----------------------------------------------------------------------------
        Algorithms:
	        Traveral all root: 
	        	make 1 as root, find all possible  -> T(0)*T(n-1)
	        	make 2 as root, find all possible  -> T(1)*T(n-2)
	        	make ..                            -> T(k)*T(n-1-k)
	        	make n as root, find all possible. -> T(n-1)*T(0)

        -----------------------------------------------------------------------------
        Demostration:
        
  	            1                2                  3                      n              
	          /  \              / \                / \                    /  \
	       T(0)  T(n-1)        1  T(n-2)         1,2  T(n-3)       1,2,3..n-1 T(0)
                               ||                 ||                     ||
                               T(1)              T(2)                  T(n-1)
        -----------------------------------------------------------------------------
        Small Knowledge:
            Q: Why List is faster than dict in python?
        	A: Concise version:
        		List: T[i] directly use index i， address = &T+i*(pointer_size)
        		Dict: T[i] hash i to index j, then address = &T+j*(pointer_size)
        		Although, both access are O(1), Dict need hash first.
        	Reference: https://stackoverflow.com/questions/53921006/why-list-is-faster-than-dict-on-the-same-python-code


        """
        T = [0]*(n+1)
        T[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                T[i] += T[j]*T[i-1-j]     
        return T[n]

    def dict_version(self,n):
        T = dict()
        T[0] = 1
        for i in range(1,n+1):
            T[i] = 0
            for j in range(i):
                T[i] += T[j]*T[i-1-j]     
        return T[n]

    def list_version(self,n):
        T = [0]*(n+1)
        T[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                T[i] += T[j]*T[i-1-j]     
        return T[n]

s= Solution()
print(s.numTrees(5))
# t = timeit.timeit(stmt="s.dict_version(100)",setup="from __main__ import Solution; s = Solution()",number=1000)
# print(t)
# t = timeit.timeit(stmt="s.list_version(100)",setup="from __main__ import Solution; s = Solution()",number=1000)
# print(t)
