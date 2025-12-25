"""
2466 统计构造好字符串的方案数
"""
from linecache import cache
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2025-12-25 优化

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        f = [1] + [0] * high
        for i in range(1, high + 1):
            if i >= zero:
                f[i] = f[i - zero]
            if i >= one:
                f[i] = (f[i] + f[i - one]) % MOD
        return sum(f[low:high + 1]) % MOD

    def countGoodStrings1(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007

        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            if i == 0:
                return 1
            return (dfs(i - zero) + dfs(i - one)) % MOD

        # ans = 0
        # for i in range(low, high + 1):
        #     ans = (ans + dfs(i)) % MOD
        return sum(dfs(i) for i in range(low, high + 1)) % MOD

    def countGoodStrings0(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        f = [0] * (high + max(zero, one) + 1)
        # 初始化
        if zero == one:
            f[zero] = 2
        else:
            f[zero], f[one] = 1, 1
        # 初始化 zero 到 one
        step = min(zero, one)
        for i in range(min(zero, one) + step, max(zero, one) + 1, step):
            f[i] += 1

        for i in range(max(zero, one) + 1, high + 1):
            f[i] = (f[i - zero] + f[i - one]) % MOD

        ans = 0
        for i in range(low, high + 1):
            ans += f[i] % MOD
        return int(ans)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    low, high, zero, one = 5, 5, 2, 4
    print(solution.countGoodStrings(low, high, zero, one))
    pass
