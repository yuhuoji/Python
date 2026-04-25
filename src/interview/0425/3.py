import sys


def solve():
    # 使用 sys.stdin.read 提高大规模数据的 I/O 效率
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2:n + 2]]

    # 找到 k 的最高有效位索引 m
    # 如果 k=0 (虽然题目说 k>=1)，bit_length()-1 会变成 -1，逻辑依然自洽
    m = k.bit_length() - 1 if k > 0 else -1

    # 确定我们需要遍历的最高位
    max_val = max(a) if a else 0
    max_bit = max(m, max_val.bit_length() - 1)

    max_sum = 0
    min_cost = 0

    # 按位独立处理
    for b in range(max_bit + 1):
        mask = 1 << b

        # 统计当前数组在第 b 位上 1 的个数
        C1 = 0
        for x in a:
            if x & mask:
                C1 += 1
        C0 = n - C1

        if b <= m:
            # 这一位可以通过操作修改
            opt1 = n // 2
            opt2 = (n + 1) // 2

            # 最大化公式的贡献
            max_pairs = opt1 * (n - opt1)
            max_sum += max_pairs * mask

            # 计算达到最优需要的最少翻转代价
            cost1 = abs(C1 - opt1) * mask
            cost2 = abs(C1 - opt2) * mask
            min_cost += min(cost1, cost2)

        else:
            # 这一位无法修改，直接计算原有贡献
            max_sum += C1 * C0 * mask

    print(f"{max_sum} {min_cost}")


# --- 本地测试用例代码 ---
def local_test():
    test_cases = [
        # 示例 1
        ("3 3\n0 1 9", "22 2"),
        # 示例 2
        ("5 109\n114 514 19 19 810", "4858 84")
    ]

    import io
    print("--- 运行测试用例 ---")
    for i, (test_in, expected) in enumerate(test_cases, 1):
        # 劫持 stdin 模拟输入
        sys.stdin = io.StringIO(test_in)
        print(f"测试例 {i}:")
        print(f"预期输出: {expected}")
        print(f"实际输出: ", end="")
        solve()
        print("-" * 20)
    # 恢复 stdin
    sys.stdin = sys.__stdin__


if __name__ == '__main__':
    # 提交到判题系统时，请注释掉 local_test()，只保留 solve()
    local_test()
    # solve()