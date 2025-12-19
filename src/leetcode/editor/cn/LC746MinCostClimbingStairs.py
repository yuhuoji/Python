"""
746 使用最小花费爬楼梯
"""
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        f = [0] * (n + 2)
        for i in range(2, n + 1):
            f[i] = min(f[i - 1] + cost[i - 1], f[i - 2] + cost[i - 2])
        return f[n]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
