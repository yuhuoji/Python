"""
419 棋盘上的战舰
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# lc200
# REVIEW @date 2026-03-11

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        seen = [[False] * n for _ in range(m)]
        direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def dfs(x: int, y: int) -> None:
            if not (0 <= x < m and 0 <= y < n and board[x][y] == 'X' and not seen[x][y]):
                return
            seen[x][y] = True
            for dir in direction:
                nx, ny = x + dir[0], y + dir[1]
                dfs(nx, ny)

        ans = 0
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if board[i][j] == 'X' and not seen[i][j]:
                    ans += 1
                    dfs(i, j)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
