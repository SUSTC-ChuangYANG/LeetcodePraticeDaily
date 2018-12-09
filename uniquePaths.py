def uniquePaths(m, n):
    """
    A robot is located at the top-left corner of a m x n grid
    (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time.
    The robot is trying to reach the bottom-right corner of the grid
    (marked 'Finish' in the diagram below).
    How many possible unique paths are there?
    :param m: row number
    :param n: line number
    :return res: totally possible unique paths
    :type m: int
    :type n: int
    :rtype: int

    Solution: use dynamic programming, build a recursion formula
              uniquePaths(m, n) = uniquePaths(m-1, n) + uniquePaths(m, n-1)
              because to locate(m, n) must go through (m,n-1) or (m-1, n)
              notice not use recursive function, it do a lot idle work.
    """
    matrix = [[1] * n for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
    return matrix[m - 1][n - 1]


print(uniquePaths(3,2))
