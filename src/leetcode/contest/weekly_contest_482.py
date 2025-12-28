"""
@date 2025-12-28
"""

import array
import bisect
import collections

from typing import *
from src.leetcode.lc_utils import *


class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * n
        prefixSum[0] = nums[0]
        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]

        suffixMin = [0] * n
        suffixMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i + 1])

        score = [0] * (n - 1)
        for i in range(0, n - 1):
            score[i] = prefixSum[i] - suffixMin[i]
        return max(score)

    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if cost1 + cost2 > costBoth:  # 使用类型 3
            ans = min(need1, need2) * costBoth
            if need1 < need2:
                need1, need2 = need2, need1
                cost1, cost2 = cost2, cost1
            if cost1 > costBoth:
                ans += (need1 - need2) * costBoth
            else:
                ans += (need1 - need2) * cost1
            return ans
        else:  # 不使用类型 3
            return need1 * cost1 + need2 * cost2

    # lc1015
    def minAllOneMultiple(self, k: int) -> int:
        # 步骤1：判断k是否含2或5的因子，若有则无解
        if k % 2 == 0 or k % 5 == 0:
            return -1

        # 步骤2：余数优化枚举全1数
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length

        # 理论上不会执行到此处（鸽巢原理保证有解）
        return -1

    def countBalanced(self, low: int, high: int) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()
    k = 47
    print(solution.minAllOneMultiple(k))
    print(111111 / 7)
    pass
