import sys

"""
5
2 5 3 1 4
5 2 4 3 1
"""
def solve():
    # 快速读取所有输入数据
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    # 预处理 p 数组中每个元素的位置
    pos_p = [0] * (n + 1)
    for i in range(n):
        val = int(input_data[1 + i])
        pos_p[val] = i

    # 预处理 q 数组中每个元素的位置
    pos_q = [0] * (n + 1)
    for i in range(n):
        val = int(input_data[1 + n + i])
        pos_q[val] = i

    ans = []
    curr_p = -1
    curr_q = -1

    # 贪心：从最大的元素 n 开始递减寻找
    for x in range(n, 0, -1):
        # 如果该元素在 p 和 q 中的位置都在当前指针之后，则合法
        if pos_p[x] > curr_p and pos_q[x] > curr_q:
            ans.append(x)
            curr_p = pos_p[x]
            curr_q = pos_q[x]

    # 输出结果
    print(len(ans))
    print(" ".join(map(str, ans)))


if __name__ == '__main__':
    solve()