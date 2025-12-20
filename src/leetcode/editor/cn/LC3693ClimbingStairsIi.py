"""
3693 爬楼梯 II
"""
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        n = len(costs)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = costs[i - 1] + min(f[i - 1] + 1, f[i - 2] + 4, f[i - 3] + 9)
        return f[n]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
