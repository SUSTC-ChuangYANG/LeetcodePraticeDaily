class Solution(object):
    def minDistance(self, word1, word2):
        """
        LongestCommon Sub-sequence Problem, just alter the output is enough.
        :param word1:
        :param word2:
        :return:
        """
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1)+1, len(word2)+1
        lcs = [[0]*l2 for _ in range(l1)]
        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i-1] == word2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + 1
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

        return l1+l2-2-(2*lcs[l1-1][l2-1])