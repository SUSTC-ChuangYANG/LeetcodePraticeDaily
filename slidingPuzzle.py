class Solution:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        import copy
        initial = tuple([item for row in board for item in row])
        if initial == (1,2,3,4,5,0):
            return 0
        start_position = None
        for i,row in enumerate(board):
            for j,item in enumerate(row):
                if item == 0:
                    start_position = (i,j)

        initial_status = {'status': initial,'pos': start_position,'board': copy.deepcopy(board),'depth':0}
        candidates = [initial_status]
        met = {initial}

        while candidates:
            x = candidates.pop(0)
            pos, board, depth = x['pos'], x['board'], x['depth']
            if self.is_valid_position((pos[0], pos[1]-1)): #  左上
                new_status, new_board, new_pos = \
                    self.swap(copy.deepcopy(board),(pos[0],pos[1]-1),pos)
                if new_status == (1,2,3,4,5,0):
                    return depth+1
                if new_status not in met:
                    met.add(new_status)
                    candidates.append({'status':new_status,'pos':new_pos,'board':new_board,'depth':depth+1})

            if self.is_valid_position((pos[0], pos[1]+1)): #  左上
                new_status, new_board, new_pos = \
                    self.swap(copy.deepcopy(board), (pos[0],pos[1]+1),pos)
                if new_status == (1,2,3,4,5,0):
                    return depth+1
                if new_status not in met:
                    met.add(new_status)
                    candidates.append({'status':new_status,'pos':new_pos,'board':new_board,'depth':depth+1})

            if self.is_valid_position((pos[0]-1, pos[1])): #  左上
                new_status, new_board, new_pos = \
                    self.swap(copy.deepcopy(board),(pos[0]-1,pos[1]),pos)
                if new_status == (1,2,3,4,5,0):
                    return depth+1
                if new_status not in met:
                    met.add(new_status)
                    candidates.append({'status':new_status,'pos':new_pos,'board':new_board,'depth':depth+1})
            if self.is_valid_position((pos[0]+1, pos[1])): #  左上
                new_status, new_board, new_pos = \
                    self.swap(copy.deepcopy(board),(pos[0]+1,pos[1]),pos)
                if new_status == (1,2,3,4,5,0):
                    return depth+1
                if new_status not in met:
                    met.add(new_status)
                    candidates.append({'status':new_status,'pos':new_pos,'board':new_board,'depth':depth+1})
        return -1

    def is_valid_position(self,position):
        if 0 <= position[0] <= 1 and 0 <= position[1] <= 2:
            return True
        else:
            return False
    def swap(self,board, source_position,des_position): # 把源位置挪到新的空位上去
        x = board[source_position[0]][source_position[1]]
        board[source_position[0]][source_position[1]] = 0
        board[des_position[0]][des_position[1]] = x
        current = tuple(board[0]) + tuple(board[1])
        return current, board, source_position





s = Solution()
print(s.slidingPuzzle([[3,2,4],[1,5,0]]))
