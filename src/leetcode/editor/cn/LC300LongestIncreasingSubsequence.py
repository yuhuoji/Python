"""
300 最长递增子序列
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[:i]):
                if y < x:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        return max(f)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
