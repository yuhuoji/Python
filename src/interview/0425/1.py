import sys

"""
5
abcxyz
aaaa
zyx
az
b
"""
def solve():
    # 使用 sys.stdin.read 提高读取大规模输入的速度
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    results = []

    for k in range(1, T + 1):
        s = input_data[k]
        n = len(s)

        # 1. 寻找第一个 >= 'n' 的字符作为起始点
        start = -1
        for i in range(n):
            if s[i] >= 'n':
                start = i
                break

        # 2. 如果全都是 'a' 到 'm'，不进行任何操作最优
        if start == -1:
            results.append(s)
            continue

        # 3. 寻找连续 >= 'n' 的字符的结束点
        end = start
        while end < n and s[end] >= 'n':
            end += 1

        # 4. 拼接字符串
        # 前缀保持不变
        prefix = s[:start]
        # 对区间 [start, end-1] 进行镜像操作
        # chr(219 - ord(c)) 等价于 'a' + ('z' - c)
        middle = "".join(chr(219 - ord(c)) for c in s[start:end])
        # 后缀保持不变
        suffix = s[end:]

        results.append(prefix + middle + suffix)

    # 一次性输出所有结果，提高 I/O 效率
    print('\n'.join(results))


# --- 本地测试用例代码 ---
def local_test():
    test_cases = [
        "abcxyz",  # 示例 1: 预期 abccba
        "aaaa",  # 示例 2: 预期 aaaa
        "zyx",  # 示例 3: 预期 abc
        "az",  # 示例 4: 预期 aa
        "b",  # 示例 5: 预期 b
        "nzmn"  # 额外测试: 预期 mamn (遇到 m 必须停止，不能把后面的 n 也拉进来导致 m 变成 n)
    ]

    print("--- 运行测试用例 ---")
    for s in test_cases:
        n = len(s)
        start = -1
        for i in range(n):
            if s[i] >= 'n':
                start = i
                break
        if start == -1:
            ans = s
        else:
            end = start
            while end < n and s[end] >= 'n':
                end += 1
            ans = s[:start] + "".join(chr(219 - ord(c)) for c in s[start:end]) + s[end:]
        print(f"输入: {s:10} -> 输出: {ans}")
    print("--------------------")


if __name__ == '__main__':
    # 提交到判题系统时，请注释掉 local_test()，只保留 solve()
    # local_test()
    solve()
