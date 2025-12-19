"""
198 打家劫舍
"""
from linecache import cache
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f0 = f1 = 0
        for i, x in enumerate(nums):
            new_f = max(x + f0, f1)
            f0 = f1
            f1 = new_f
        return f1

    def rob3(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 2)
        for i, x in enumerate(nums):
            f[i] = max(x + f[i - 2], f[i - 1])
        return f[n - 1]

    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 2)
        for i, x in enumerate(nums):
            f[i + 2] = max(x + f[i], f[i + 1])
        return f[n + 1]

    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n

        def dfs(i):
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
            res = max(dfs(i - 1), nums[i] + dfs(i - 2))
            cache[i] = res
            return res

        return dfs(n - 1)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
