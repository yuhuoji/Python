import sys
import bisect

"""
1
3 1
4 2 3
"""
def solve():
    # 使用 sys.stdin.read 一次性读取，解决大规模输入输出的耗时问题
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1

    out = []
    for _ in range(T):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2

        a = []
        for _ in range(n):
            a.append(int(input_data[idx]))
            idx += 1

        # ans[m] 记录保留 m 个元素的最小代价，初始化为无穷大
        ans = [float('inf')] * (n + 1)

        # 动态维护当前前缀的有序列表
        sorted_a = []

        # 遍历所有可能的前缀长度 R
        for R in range(1, n + 1):
            # 将当前新元素插入到有序列表中，保持升序
            bisect.insort(sorted_a, a[R - 1])

            # current_sum 用于累加前 m 个最小元素的值
            current_sum = 0

            # 对于当前长度为 R 的前缀，尝试更新所有可能的 m (1 <= m <= R)
            for m in range(1, R + 1):
                current_sum += sorted_a[m - 1]
                # 计算代价：删除的个数 (R - m) * k + 选中的 m 个元素的权重和
                cost = (R - m) * k + current_sum

                # 更新保留 m 个元素的历史最低代价
                if cost < ans[m]:
                    ans[m] = cost

        # 忽略 ans[0]，将 ans[1...n] 转换为字符串输出
        out.append(" ".join(map(str, ans[1:])))

    # 一次性打印所有结果
    print("\n".join(out))


if __name__ == '__main__':
    solve()