"""
1905 统计子岛屿
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *

"""
子岛屿
在grid2中的岛屿，并完全包含在grid1中
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    ok = True

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        seen = [[False] * n for _ in range(m)]  # grid2
        direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def dfs(x: int, y: int) -> None:

            if not (0 <= x < m and 0 <= y < n and grid2[x][y] == 1 and not seen[x][y]):
                return
            if grid1[x][y] == 0:  # 如果grid1对应位置为水则不行
                self.ok = False
            seen[x][y] = True
            for dir in direction:
                nx, ny = x + dir[0], y + dir[1]
                dfs(nx, ny)

        ans = 0
        for i, row in enumerate(grid2):
            for j, c in enumerate(row):
                if grid2[i][j] == 1 and not seen[i][j] and grid1[i][j] == 1:  # 可能是子岛屿
                    self.ok = True
                    dfs(i, j)
                    ans += 1 if self.ok else 0
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
