"""
503 下一个更大元素 II
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 从右向左 栈中记录下一个更大元素的候选项
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk = []
        ans = [-1] * n
        for i in range(2 * n - 1, -1, -1):
            x = nums[i % n]
            while stk and x > stk[-1]:
                stk.pop()
            if stk and i < n:  # 只在
                ans[i] = stk[-1]
            stk.append(x)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
