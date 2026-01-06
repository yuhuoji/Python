"""
62 不同路径
"""
from linecache import cache
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [0] * (n + 1)
        f[1] = 1
        for _ in range(m):
            for j in range(n):
                f[j + 1] += f[j]
        return f[n]

    def uniquePaths2(self, m: int, n: int) -> int:
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 1
        for i in range(m):
            for j in range(n):
                f[i + 1][j + 1] = f[i + 1][j] + f[i][j + 1]
        return f[m][n]

    def uniquePaths1(self, m: int, n: int) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0 or j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)

        return dfs(m - 1, n - 1)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
