"""
136 只出现一次的数字
"""
from functools import reduce
from linecache import cache
from math import inf
from operator import xor
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ans = 0
        # for x in nums:
        #     ans ^= x
        # return ans
        return reduce(xor, nums)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
