"""
53 最大子数组和
"""
import ast
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        for i in range(n):
            f[i] = max(f[i - 1], 0) + nums[i]
        return max(f)

    def maxSubArray1(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        f[0] = 0
        for i in range(len(nums)):
            f[i] = max(f[i - 1], 0) + nums[i]
        return max(f)

    def maxSubArray2(self, nums: List[int]) -> int:
        ans = -inf
        f = 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans

    # 前缀和
    def maxSubArray3(self, nums: List[int]) -> int:
        ans = -inf
        min_pre_sum = pre_sum = 0
        for x in nums:
            pre_sum += x
            ans = max(ans, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    intput = "[-2,1,-3,4,-1,2,1,-5,4]"
    print(solution.maxSubArray(ast.literal_eval(intput)))
    pass
