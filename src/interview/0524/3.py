"""
示例输入1：
3
2 5 20

示例输出1：
5

示例输入2：
10
1 100 1 1 1 90 1 1 80 1

示例输出2：
6
"""

import sys


def min_cost_climbing_stairs(cost):
    n = len(cost)
    # dp0 表示到达当前位置前两个位置的最小花费
    # dp1 表示到达当前位置前一个位置的最小花费
    # 到达第 0 个或第 1 个台阶本身不需要花费，因为可以直接选择从 0 或 1 开始
    dp0 = 0
    dp1 = 0
    # 计算到达第 i 个位置的最小花费
    # i == n 时表示到达楼梯顶部
    for i in range(2, n + 1):
        cur = min(dp1 + cost[i - 1], dp0 + cost[i - 2])
        dp0 = dp1
        dp1 = cur
    return dp1
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    cost = list(map(int, data[1:1 + n]))
    print(min_cost_climbing_stairs(cost))

if __name__ == "__main__":
    main()