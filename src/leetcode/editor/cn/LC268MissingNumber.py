"""
268 丢失的数字
"""
from functools import reduce
from linecache import cache
from math import inf
from operator import xor
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 数组哈希
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        has = [False] * (n + 1)
        for i in range(n):
            has[nums[i]] = True
        for i in range(n):
            if not has[i]:
                return i
        return n

    # 位运算
    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        a = reduce(xor, range(0, n + 1))
        b = reduce(xor, nums)
        return a ^ b

    # 数学计算
    def missingNumber1(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n * (n + 1) / 2 - sum(nums))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    n = 10
    ans1 = reduce(xor, range(1, n + 1), 0)
    ans2 = reduce(xor, range(0, n + 1))
    print(f"ans1 = {ans1}, ans2 = {ans2}")
    pass
