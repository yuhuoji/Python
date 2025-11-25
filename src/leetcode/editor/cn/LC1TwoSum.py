"""
1 两数之和
"""
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums
        :type target: int
        :rtype: List[int]
        """
        idx = {}
        for i , x in enumerate(nums):
            if target - x in idx:
                return [idx[target - x], i]
            idx[x] = i
        return []
# leetcode submit region end(Prohibit modification and deletion)
