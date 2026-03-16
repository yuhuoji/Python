"""
2087 网格图中机器人回家的最小代价
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        sx, sy = startPos
        ex, ey = homePos

        res = 0

        if ex > sx:
            res += sum(rowCosts[sx + 1: ex + 1])
        else:
            res += sum(rowCosts[ex: sx])

        if ey > sy:
            res += sum(colCosts[sy + 1: ey + 1])
        else:
            res += sum(colCosts[ey: sy])

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
