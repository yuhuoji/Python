import sys

"""
3
3 2
5 2 7
4 3
0 0 0 0
2 5
10 1
别随便改变量名， min max都是保留字，可能出错，可以用mn mx
"""
def solve():
    # 使用生成器按需读取 token，极大地优化了空间复杂度，避免一次性读入超大列表
    def get_ints():
        for line in sys.stdin:
            for token in line.split():
                yield int(token)

    tokens = get_ints()

    # try:
    T = next(tokens)
    # except StopIteration:
    #     return

    out = []
    for _ in range(T):
        n = next(tokens)
        k = next(tokens)

        min_candies = 0
        extra_candies = 0

        for _ in range(n):
            c_i = next(tokens)

            # 累加基础份额
            min_candies += c_i // k

            # 如果有剩余，意味着在最佳情况下该小朋友可以多拿1颗
            if c_i % k != 0:
                extra_candies += 1

        max_candies = min_candies + extra_candies
        out.append(f"{min_candies} {max_candies}")

    # 一次性输出结果，减少 I/O 阻塞时间
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    solve()