import time
class Solution:
    def partition(self, s):
        """
        Problem Description:
            Given a string s, partition s such that every substring of the partition is a palindrome.
            Return all possible palindrome partitioning of s.
        Solution: DFS and pruning
        Pruning principle. Judge if a sub-string is palindrome. if yes, it could be a node.
        The basic idea is the same as restoreIPAddress.


        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.recursive_partition(s=s, temp=[], res=res)
        return res

    def recursive_partition(self, s, temp, res):
        if not s:
            res.append(temp.copy())
            return

        for i in range(len(s)):
            if self.is_palindrome_2(s[0:i + 1]):
                temp.append(s[0:i + 1])
                self.recursive_partition(s=s[i+1:], temp=temp, res=res)
                temp.pop()

    @staticmethod
    def is_palindrome(s):
        i, j = 0, len(s)-1
        while i <= j:
            if s[j] != s[i]:
                return False
            i += 1
            j -= 1
        return True

    @staticmethod         # this is a faster version than above one, because C optimization.
    def is_palindrome_2(s):
        return s[::-1] == s





s = Solution()
start = time.time()
res = s.partition("avcvvcva")
end = time.time()
print(end-start)
# print(res)