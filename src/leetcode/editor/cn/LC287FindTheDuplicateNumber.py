"""
287 寻找重复数
"""
from linecache import cache
from math import inf
from typing import *
from src.leetcode.lc_utils import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                fast = 0
                while fast != slow:
                    fast = nums[fast]
                    slow = nums[slow]
                return slow
        return -1

    def findDuplicate1(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()

    pass
