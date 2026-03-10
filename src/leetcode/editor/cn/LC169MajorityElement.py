"""
169 多数元素
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = hp = 0
        for x in nums:
            if hp == 0:
                ans, hp = x, 1
            else:
                hp += 1 if x == ans else -1
        return ans

    def majorityElement1(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
