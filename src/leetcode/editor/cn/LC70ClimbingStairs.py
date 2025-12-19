"""
70 爬楼梯
"""
from typing import *
from src.leetcode.lc_utils import *

# TODO @date 2025-12-19 六、矩阵快速幂优化

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs2(self, n: int) -> int:
        f0 = 1
        f1 = 1
        for i in range(2, n + 1):
            new_f = f0 + f1
            f0 = f1
            f1 = new_f
        return f1

    # f(i) = f(i-1) + f(i-2)
    def climbStairs(self, n: int) -> int:
        f = [0] * (n + 2)
        f[0] = f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]
    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
