class Solution:
    def restoreIpAddresses(self, s):
        """
        Given a string containing only digits, restore it by
        returning all possible valid IP address combinations.
        Solution: Use backtracking.

        Solution: DFS and Pruning
        for each parent node, there are three child node
                        10
                     /  |  \
                    /   |   \
                   2   25   255
        They are continue three numbers.
        The Pruning conditions including:
        a)  the rest position left can not satisfy the rest numbers. E.g. ['2','5','5'] and "552334"
        b)  the node's number is illegal. e.g. '345'.
        The stop condition is : the rest position and the rest numbers both zero.

        :type s: str
        :rtype: List[str]
        """
        res =[]
        self.backtracking(s,res,[],4)
        return res

    def backtracking(self, s, res, tmp, p):
        l = len(s)
        x = 3 if l > 3 else l
        for i in range(x):
            if self.valid_ip(s[0:i+1]):  # at most three child node
                candidate = s[i + 1:]
                position_left = p - 1
                if position_left and candidate:  # 有位置剩下，有内容
                    if 3*position_left >= len(candidate):  # 剩余的位置可以装下
                        tmp.append(s[0:i + 1])  # parent node
                        self.backtracking(s[i + 1:], res, tmp, position_left)
                        tmp.pop()
                    continue
                if position_left == 0 and not candidate: # 没位置剩下，没内容
                    res.append('.'.join(tmp)+"."+s[0:i+1])
                # 有位置剩下，有内容 do nothing，因为遇到的时候已经到末尾了。
             else:
                return

    @staticmethod
    def valid_ip(s):
        if len(s) > 1 and s[0]=='0':
            return False
        if int(s) > 255:
            return False
        else:
            return True

s = Solution()
res = s.restoreIpAddresses("1111")
print(res)