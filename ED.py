class Solution(object):
    """
    从后往前看，对于最后一个字符，如果相等，直接看回[i-1,j-1]
    如果不想等，有三种解决办法，增删改。
    无论如何增删改其一必然是要做的，如果不做，最后一位永远都不会和目标的末尾一致。
    因此，分别做
         增，一步到位，和最后一位一样，接下来要处理的就剩下 [i, j-1]
         删，删掉最后一个，之后就聚焦在[i-1, j]
         改，一步到位，和最后一位一样，加下来要处理的就剩下 [i-1,j]
    关于DP: dp的核心就在于记忆，或者说缓存，把以前算过的记下来。也可以叫做带记忆的递归【BoHuang】
    """
    def minDistance_recursive(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        if l1 == 0:
            return l2
        if l2 == 0:
            return l1
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:],word2[1:])
        else:
            insert = 1 + self.minDistance(word1, word2[1:])
            delete = 1 + self.minDistance(word1[1:], word2)
            replace = 1 + self.minDistance(word1[1:],word2[1:])
            return min(insert,delete,replace)

    def minDistance_dp(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        md = [[0 for i in range(l2+1)] for j in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i == 0:
                    md[i][j] = j
                    continue
                if j == 0:
                    md[i][j] = i
                    continue

                if word1[i-1] == word2[j-1]:
                    md[i][j] = md[i-1][j-1]
                else:
                    insert = md[i][j-1] + 1
                    delete = md[i-1][j] + 1
                    replace = md[i-1][j-1] + 1
                    md[i][j] = min(insert,delete,replace)

        return md[l1][l2]




s = Solution()
print(s.minDistance_dp("intention","execution"))