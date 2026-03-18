"""
10
5
3 4 5 6 7
1 2 3 5 5
2 3 4 5 6
"""

import sys

def solve():
    # 按行读取并过滤空行
    input_lines = [line.strip() for line in
                   sys.stdin.read().strip().split('\n') if line.strip()]
    if not input_lines:
        return

    # 解析 m 和 n
    m = int(input_lines[0])
    n = int(input_lines[1])

    # 解析三个数组
    spaces = [int(x) for x in input_lines[2].split()]
    swap_costs = [int(x) for x in input_lines[3].split()]
    recompute_costs = [int(x) for x in input_lines[4].split()]

    # 贪心：预处理每个张量的最小代价
    costs = [min(swap_costs[i], recompute_costs[i]) for i in range(n)]

    # 边界情况：所有张量全用上也达不到目标空间 m
    if sum(spaces) < m:
        print("error")
        return

    # 初始化 DP 数组
    INF = float('inf')
    dp = [INF] * (m + 1)
    dp[0] = 0  # 释放 0 空间的代价是 0

    # 动态规划求解 (0-1 背包变种)
    for w, c in zip(spaces, costs):
        # 必须倒序遍历，保证每个张量只被使用一次
        for j in range(m, -1, -1):
            # 如果当前需求 j 小于张量大小 w，说明这一个张量就能满足需求，相当于只需要前置 0 空间
            needed = j - w if j > w else 0

            # 状态转移：取当前代价和“加上这个张量后的代价”的最小值
            if dp[needed] + c < dp[j]:
                dp[j] = dp[needed] + c

    # 输出结果
    if dp[m] != INF:
        print(dp[m])
    else:
        print("error")


if __name__ == '__main__':
    # 你这单引号是不是写成反引号了？
    solve()