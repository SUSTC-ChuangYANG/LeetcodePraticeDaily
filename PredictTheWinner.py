class Solution:
    def PredictTheWinner(self, nums):
        """
        Problem Description:

        Idea: use game theory
        :type nums: List[int]
        :rtype: bool
        """
        self.nums = nums
        alpha = -float('inf')
        beta = float('inf')
        return self.alphabeta(0, alpha, beta, True, up=0, down=len(nums)-1) >= 0


    def alphabeta(self,score, alpha, beta, maximizingPlayer,up, down):
        if up == down:
            return score
        if maximizingPlayer:
            new_score = score + self.nums[up]
            value = self.alphabeta(new_score, alpha, beta, False, up+1, down)
            if value >= 0:
                return 1
            alpha = max(alpha, value)
            if alpha >= beta:
                return value
            new_score = score + self.nums[down]
            value = max(value, self.alphabeta(new_score, alpha, beta, False, up, down-1))
        else:
            new_score = score - self.nums[up]
            value = self.alphabeta(new_score, alpha, beta, True, up=up + 1, down=down)
            beta = min(beta, value)
            if value < 0:
                return -1
            if alpha >= beta:
                return value
            new_score = score - self.nums[down]
            value = min(value, self.alphabeta(new_score, alpha, beta, True, up=up, down=down - 1))

        return value

    @staticmethod
    def dynamic_programming(nums):
        length = len(nums)
        if length == 1:
            return nums[0]>=0
        dp = [[0 for i in range(length)] for i in range(length)]

        for i in range(length):
            dp[i][i] = nums[i]
        for k in range(1,length):
            i, j = 0, k
            while j <= length-1:
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
                i, j = i+1, j+1 
        return dp[0][length-1] >=0
    def dynamic_programming_super(nums):
        length = len(nums)
        if length == 1:
            return nums[0]>=0
        i = length - 1
        while i >=0:
            j = i
            while j <= length - 1:
                if i == j:
                    dp[i] = nums[i]
                else:
                    dp[j] = max(nums[i]-dp[j], nums[j]- dp[j-1])


        for i in range()

     def alphabeta(self,score, maximizingPlayer,up, down):
        if up == down:
            return score
        if maximizingPlayer:
            value = self.alphabeta(score + self.nums[up], False, up+1, down)
            if value >= 0:
                return 1
            value = max(value, self.alphabeta(score + self.nums[down], False, up, down-1))
        else:
            value = self.alphabeta(score - self.nums[up], True, up + 1,down)
            if value < 0:
                return -1
            value = min(value, self.alphabeta(score - self.nums[down], True, up, down - 1))

        return value


s = Solution()
print(s.PredictTheWinner([1,5,2]))



