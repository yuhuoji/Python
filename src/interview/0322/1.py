import sys


"""
2
36 15
结果114
"""
def solve():
    # 使用 sys.stdin.read 一次性读取所有输入，极大提升 I/O 速度
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    nums = input_data[1:]

    # 统计数字 1-9 的出现频次 (下标 1 代表字符 '1')
    digit_counts = [0] * 10

    # 统计各个数位的容量需求。题目中 a_i <= 10^9，最长为 9 位 (因为不含0)
    # place_counts[i] 表示权重为 10^i 的数位有多少个
    place_counts = [0] * 10

    # 1. 收集数据：统计字符频次和数位容量
    for num_str in nums:
        length = len(num_str)
        # 统计每个字符的数量
        for char in num_str:
            digit_counts[int(char)] += 1

        # 统计数位需求：长度为 L 的数字，贡献了 10^0, 10^1 ... 10^(L-1) 各一个位置
        for i in range(length):
            place_counts[i] += 1

    total_sum = 0
    current_digit = 9  # 从最大的数字 9 开始贪心分配

    # 2. 贪心分配：从最高位 (10^9) 到最低位 (10^0) 依次分配最大的可用数字
    for p in range(9, -1, -1):
        needed = place_counts[p]
        if needed == 0:
            continue

        multiplier = 10 ** p

        # 当这个数位还需要数字时，不断从手里最大的数字开始填补
        while needed > 0:
            # 找到当前手里最大的可用数字
            while current_digit > 0 and digit_counts[current_digit] == 0:
                current_digit -= 1

            if current_digit == 0:  # 题目保证不含'0'，理论上不会走到这里
                break

            # 决定这次可以填入多少个 current_digit
            take = min(needed, digit_counts[current_digit])

            # 累加到总和中
            total_sum += take * current_digit * multiplier

            # 更新库存和需求
            digit_counts[current_digit] -= take
            needed -= take

    print(total_sum)


if __name__ == '__main__':
    solve()