import sys

"""
5
1
2
3
4
5
"""
def solve():
    # 快速读取所有数据，优化 I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    queries = [int(x) for x in input_data[1:t + 1]]

    # 设定最大位数 L = 22 (根据提示 10^18 项约 20 位，22 位绰绰有余)
    L = 22

    # dp[i][j] 表示长度为 i 的由非 '3' 构成的数字串，各位数字之和 mod 3 == j 的方案数
    dp = [[0] * 3 for _ in range(L + 1)]
    dp[0][0] = 1  # 长度为 0 时，和为 0，这是一种合法的基础状态

    for i in range(1, L + 1):
        for j in range(3):
            for d in range(10):
                if d == 3:
                    continue
                # 填入数字 d，状态转移
                dp[i][(j + d) % 3] += dp[i - 1][j]

    out = []

    # 回答每一次查询
    for k in queries:
        ans = []
        cur_rem = 0  # 记录当前已确定前缀的各位数字之和 mod 3 的结果

        # 从最高位开始往下试探
        for i in range(L - 1, -1, -1):
            for d in range(10):
                if d == 3:
                    continue

                # 统计如果当前位填入 d，后续长度为 i 的后缀能提供多少个最终 mod 3 不为 0 的方案
                count_valid = 0
                for target_rem in (1, 2):  # 最终整除 3 的余数必须是 1 或 2
                    needed_rem = (target_rem - cur_rem - d) % 3
                    count_valid += dp[i][needed_rem]

                # 判断第 k 个数是否落在当前分支内
                if k <= count_valid:
                    ans.append(str(d))
                    cur_rem = (cur_rem + d) % 3
                    break
                else:
                    k -= count_valid

        # 得到的是定长的 22 位字符（包含前导零），去掉前导零即为正确答案
        out.append("".join(ans).lstrip('0'))

    # 一次性输出，减少阻塞
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    solve()