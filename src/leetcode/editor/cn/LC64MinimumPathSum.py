"""
64 最小路径和
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minPathSum3(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [inf] * (n + 1)
        f[1] = 0  # 简便[0][0]特判
        for i in range(m):
            for j in range(n):
                f[j + 1] = min(f[j + 1], f[j]) + grid[i][j]
        return f[n]

    # 递推
    def minPathSum2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 0  # 简便[0][0]特判
        for i in range(m):
            for j in range(n):
                f[i + 1][j + 1] = min(f[i][j + 1], f[i + 1][j]) + grid[i][j]
        return f[m][n]

    # 使用负数索引
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        f[0][-1] = 0  # 简便[0][0]特判
        for i in range(m):
            for j in range(n):
                f[i][j] = min(f[i][j - 1], f[i - 1][j]) + grid[i][j]
        return f[m - 1][n - 1]

    # 递归
    def minPathSum1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return grid[0][0]
            return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]

        return dfs(m - 1, n - 1)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
