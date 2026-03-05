"""
137 只出现一次的数字 II
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# REVIEW @date 2026-03-05
# TODO @date 2026-03-05 出现5次

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for x in nums:
            b = (b ^ x) & ~a
            a = (a ^ x) & ~b
        return b

    # leetcode submit region end(Prohibit modification and deletion)

    def fun(self, nums: List[int]) -> int:
        a = b = c = 0
        for x in nums:
            b = (b ^ x) & ~a
            a = (a ^ x) & ~b
        return b


if __name__ == '__main__':
    solution = Solution()

    pass
