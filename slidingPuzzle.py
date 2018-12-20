class Solution:
    met = {}
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        initial = tuple([item for row in board for item in row])
        for i,row in enumerate(board):
            for j,item in enumerate(row):
                if item == 0:
                    start_position = (i,j)
        initial_status = {'status':initial,'pos':start_position}
        depth = 0
        candidate = [initial_status]
        met = {initial}
        while candidate:
            x = candidate.pop()
            cur_pos = x[pos]
            if self.is_valid_position((cur_pos[0]-1,cur_pos[1]-1)): #  左上


        if is_valid(initial):
            print("他妈的都不用找，找个锤子")
            return 0

        for i,row in enumerate(board):
            for j,item in enumerate(row):
                if item == 0:
                    start_position = (i,j)


        # 这才是正常道路
        met.add(initial)
        return self.search(board, met, depth=0, start_position=start_position)

    def search(self, board, met, depth, start_position):
        # 左上角
        left_up = (start_position[0]-1, start_position[1]-1)
        # 该位置有效
        if self.is_valid_position(left_up):
            # 交换
            self.swap(board=board, start_position = start_position,des_position=left_up)
            #
            current = self.is_met(board=board, met=met)
            # 如果当前的局势已经出现过，
                    # 这是一个可达路径， 直接进行深度拼接
                    # 这是一个环，剪掉

            # 如果当前的局势从未见过
            if current:
                met.add(current)
                return self.search(board, met, depth=depth+1, start_position=left_up)
            else:
                self.swap(board=board, start_position=left_up, des_position=start_position)

        if self.is_valid_position(start_position):

            self.search()
        else:
            return
        empty_position = None
        for i,row in enumerate(board):
            for j,item in enumerate(row):
                if item == 0:
                    empty_position = (i,j)
                    break
        if empty_position[0]-1 > 0 and empty_position[1]-1 > 0:  # 左上角

            x = board[empty_position[0]-1][empty_position[1]-1]
            board[empty_position[0] - 1][empty_position[1] - 1] = 0
            board[empty_position[0]][empty_position[1]] = x
            current = tuple([item for row in board for item in row])
            if current not in met:
                met.add(current)
                if is_vaild(current):
                    return step
        # if empty_position[0]-1>=0 and empty_position[1]-1>=0

    def is_valid_position(self,position):

        if 0 <= position[0] <= 1 and 0 <= position[1] <=2:
            return True
        else:
            return False
    def swap(self,board, source_position, des_position):
        x = board[source_position[0]][source_position[1]]
        board[source_position[0]][source_position[1]] = 0
        board[des_position[0]][des_position[1]] = x

    def is_met(self,board, met):
        current = tuple([item for row in board for item in row])
        if current in met:
            return None
        else:
            return current





s = Solution()
# s.slidingPuzzle([[1,3,3],[4,5,0]])
print(s.valid_position((0,-1)))