"""
213 打家劫舍 II
"""
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2025-12-23 分治 数组切片方法

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob198(self, nums: List[int]) -> int:
            n = len(nums)
            f = [0] * (n + 2)
            for i, x in enumerate(nums):
                f[i] = max(x + f[i - 2], f[i - 1])
            return f[n - 1]

        return max(nums[0] + rob198(nums[2:-1]), rob198(nums[1:]))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
