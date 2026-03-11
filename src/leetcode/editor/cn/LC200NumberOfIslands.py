"""
200 岛屿数量
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]
        direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def dfs(x: int, y: int) -> None:
            """
            1. 范围之内
            2. 是陆地
            3. 没访问过
            """
            if not (0 <= x < m and 0 <= y < n and grid[x][y] == '1' and not seen[x][y]):
                return
            seen[x][y] = True
            for dir in direction:
                nx, ny = x + dir[0], y + dir[1]
                dfs(nx, ny)

        ans = 0
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if grid[i][j] == '1' and not seen[i][j]:
                    ans += 1
                    dfs(i, j)
        return ans

        # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
