"""
53 最大子数组和
"""
import ast
from cmath import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1], 0) + nums[i]
        return max(f)

    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        f = 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    intput = "[-2,1,-3,4,-1,2,1,-5,4]"
    print(solution.maxSubArray(ast.literal_eval(intput)))
    pass
