class Solution:
    def slidingPuzzle(self, board):
        """
        Problem Description:
        On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square repr-
        -esented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
        The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
        Given a puzzle board, return the least number of moves required so that the state of the board is 
        solved. If it is impossible for the state of the board to be solved, return -1.
        
        Solution:
        ----------------------------------------------------------------------------------------------------
        广度优先搜索，BFS.
        a. 因为我们要找的是最短距离，所以广搜很合适。 
        b. 每一层的node 代表一种unique的node。
        c. 所谓不走回头路，相同的节点不能出现两次，如果一个节点再次被搜索到，直接跳过，因为已经有了距离更短的,这成环了。
        -----------------------------------------------------------------------------------------------------
        layer0                start_node
        layer1        node1    node2    node3   node4
        layer2               node5    node6
        layer3            node7    node8    node9 
        layer4               node10 (bingo!)
        ----------------------------------------------------------------------------------------------------
        Notice:
        (1) 注意存储棋盘的时候用string 或者list(向量),这样比用矩阵会快很多。 deepcopy 复制矩阵之后调整落子位置，很慢。
        ----------------------------------------------------------------------------------------------------
        Attachment:
        A* algorithms pseudo-code: best_first_graph_search
        曼哈顿距离：出租车距离 https://blog.csdn.net/CQBZLYTina/article/details/75149587
        ----------------------------------------------------------------------------------------------------

        :type board: List[List[int]]
        :rtype: int
        """
        goal = "123450"
        initial = ''.join([str(item) for row in board for item in row])
        if initial == goal:
            return 0
        transfer_matrix = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]

        # find initial empty position index 
        for i,row in enumerate(board):
            for j,item in enumerate(row):
                if item == 0:
                    start_pos = i*3+j

        # initial closed and candidates
        # closed = {initial}
        closed = set()
        closed.add(initial)
        initial_node = {'status':initial,'pos':start_pos,'depth':0}
        candidates = [initial_node]

        while candidates:
            node = candidates.pop(0) # 其他人这里也是pop(0) 吗
            status, pos, depth = node['status'], node['pos'], node['depth']
            
            src_status = list(status)
            for candi_pos in transfer_matrix[pos]:
                new_status = src_status[:]
                new_status[pos] = new_status[candi_pos]
                new_status[candi_pos] = '0'
                new_status = ''.join(new_status)
                if new_status == goal:
                    return depth+1
                if new_status not in closed:
                    closed.add(new_status)
                    candidates.append({'status':new_status,'pos':candi_pos,'depth':depth+1})
        return -1

    @staticmethod
    def best_first_graph_search(problem, f):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
        f = memoize(f, 'f')
        node = Node(problem.initial)
        frontier = PriorityQueue('min', f)
        frontier.append(node)
        explored = set()
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            explored.add(node.state)
            for child in node.expand(problem):
                if child.state not in explored and child not in frontier:
                    frontier.append(child)
                elif child in frontier:
                    incumbent = frontier[child]
                    if f(child) < f(incumbent):
                        del frontier[incumbent]
                        frontier.append(child)
        return None





s = Solution()
print(s.slidingPuzzle([[3,2,4],[1,5,0]]))

