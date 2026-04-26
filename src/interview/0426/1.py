import sys


def solve():
    # 读取标准输入中的所有内容
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # 解析输入 n: 任务数, m: 总 token 预算, t: 总时间预算
    n = int(input_data[0])
    m = int(input_data[1])
    t = int(input_data[2])

    tasks = []
    idx = 3
    for _ in range(n):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        d = int(input_data[idx + 3])
        tasks.append((a, b, c, d))
        idx += 4

    # 初始化 DP 表：dp[j][k] 表示花费不超过 j 个 token 和 k 的时间能完成的最大任务数
    dp = [[0] * (t + 1) for _ in range(m + 1)]

    for a, b, c, d in tasks:
        # 0-1背包问题压缩空间后，为了防止重复选择同一个任务，必须倒序遍历
        # 性能优化：题目限制了 c < a 且 b < d，因此最低的 token 开销是 c，最低的时间开销是 b。
        # 如果 j < c 或 k < b，则当前预算无法执行该任务的任何一种模式，可直接截断内层循环。
        for j in range(m, c - 1, -1):
            for k in range(t, b - 1, -1):
                max_tasks = dp[j][k]

                # 尝试选项 1：常规模式
                if j >= a and k >= b:
                    if dp[j - a][k - b] + 1 > max_tasks:
                        max_tasks = dp[j - a][k - b] + 1

                # 尝试选项 2：降耗模式
                if j >= c and k >= d:
                    if dp[j - c][k - d] + 1 > max_tasks:
                        max_tasks = dp[j - c][k - d] + 1

                dp[j][k] = max_tasks

    # 输出在最大预算 m 和 t 下的结果
    print(dp[m][t])


if __name__ == '__main__':
    solve()

    """
3 10 10
5 5 2 8
4 3 3 5
8 2 4 6
    """