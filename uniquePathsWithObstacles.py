def uniquePathsWithObstacles(obstacleGrid):
    """
    Problem Description:
        A robot is located at the top-left corner of a m x n grid
        (marked 'Start' in the diagram below).The robot can only
        move either down or right at any point in time. The robot
        is trying to reach the bottom-right corner of the grid
        (marked 'Finish' in the diagram below).
        Now consider if some obstacles are added to the grids.
        How many unique paths would there be?
        source: https://leetcode.com/problems/unique-paths-ii/
    :param obstacleGrid: 2-d list array, An obstacle and empty space
                         is marked as 1 and 0 respectively in the grid.
    :type obstacleGrid: List[List[int]]
    :rtype: int
    Solution: dynamic programming, set all obstacles as 0
    """

    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    matrix = [[0] * n for i in range(m)]
    for j in range(n):
        if obstacleGrid[0][j] != 1:
            matrix[0][j] = 1
        else:
            break
    for i in range(m):
        if obstacleGrid[i][0] != 1:
            matrix[i][0] = 1
        else:
            break

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] != 1:
                matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
    return matrix[m - 1][n - 1]