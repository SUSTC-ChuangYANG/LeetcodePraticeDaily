class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        l1, l2 = len(text1)+1, len(text2)+1
        lcs = [[0 for i in range(l2)] for j in range(l1)]
        for i in range(1, l1):
            for j in range(1, l2):
                if text1[i-1] == text2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

        print(lcs[l1-1][l2-1])






s = Solution()
s.longestCommonSubsequence("abc","def")
