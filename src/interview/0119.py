from typing import List


def singleNumber(nums: List[int]) -> int:
    """
    找出数组中只出现一次的元素，其余元素均出现三次。
    方法：位运算（有限状态机）
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    ones, twos = 0, 0

    for num in nums:
        # 1. 更新 ones:
        # (ones ^ num) 模拟无进位加法
        # & ~twos 的含义是：如果这个位已经出现过两次了(twos为1)，
        # 加上这次就是第三次，需要抵消归零，所以要把 ones 里的这一位强行置 0
        ones = (ones ^ num) & ~twos

        # 2. 更新 twos:
        # 同理，(twos ^ num) 尝试将位放入 twos
        # & ~ones 的含义是：如果这个位刚刚被放入 ones (说明目前是出现1次的状态)，
        # 那么它肯定不是出现2次的状态，需要把 twos 里的这一位保持为 0
        twos = (twos ^ num) & ~ones
        print(ones, twos)

    # 最后只出现一次的数字会停留在 ones 中
    # (如果题目改为“其余出现3次，这就找出那个出现2次的”，则返回 twos)
    return ones


if __name__ == "__main__":
    # --- 测试用例 ---

    # 用例 1: 标准测试
    test_1 = [2, 2, 3, 2]
    print(f"输入: {test_1}")
    print(f"输出: {singleNumber(test_1)}")  # 预期输出: 3
    print("-" * 20)

    # 用例 2: 包含多个干扰项
    test_2 = [0, 1, 0, 1, 0, 1, 99]
    print(f"输入: {test_2}")
    print(f"输出: {singleNumber(test_2)}")  # 预期输出: 99
    print("-" * 20)

    # 用例 3: 包含负数 (Python位运算处理负数需要注意，但此算法原生支持)
    test_3 = [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]
    print(f"输入: {test_3}")
    print(f"输出: {singleNumber(test_3)}")  # 预期输出: -4