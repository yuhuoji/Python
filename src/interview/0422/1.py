import sys


def solve():
    # 严格采用要求的输入输出模板读取所有行
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    ptr = 0

    # 循环处理所有测试用例（机考系统可能会把多个用例拼接在一起传入）
    while ptr < len(lines):
        # 1. 解析基础参数
        parts = lines[ptr].split()
        N = int(parts[0])
        c_dist = int(parts[1])
        w_threshold = int(parts[2])
        ptr += 1

        # 解析基站详情
        nodes = []
        for _ in range(N):
            x, y, t, w, users = map(int, lines[ptr].split())
            nodes.append((x, y, t, w, users))
            ptr += 1

        # 2. 计算基站间的直接关联关系 (曼哈顿距离 <= c_dist)
        # associated[i][j] 为 True 表示节点 i 和 j 直接关联
        associated = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                dist = abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1])
                if dist <= c_dist:
                    associated[i][j] = True

        # 3. 识别关键节点
        key_nodes = []
        for i in range(N):
            load_sum = 0
            for j in range(N):
                if associated[i][j]:
                    load_sum += nodes[j][3]  # 累加直接关联基站的负载 w

            if load_sum >= w_threshold:
                key_nodes.append(i)  # 记录关键节点的原始索引

        # 如果全网无关键节点，直接输出 0 并进入下一个用例
        if not key_nodes:
            print(0)
            continue

        # 4. 按照发生时间 t 升序排序，作为 DAG 的拓扑序
        # nodes[idx][2] 取的是时间 t
        key_nodes.sort(key=lambda idx: nodes[idx][2])

        # 5. 动态规划寻找最大用户路径
        # dp 数组记录以每个关键节点为终点的最大用户数，初始为自身的用户数 (nodes[idx][4])
        dp = [nodes[idx][4] for idx in key_nodes]
        max_total_users = 0

        for i in range(len(key_nodes)):
            curr_idx = key_nodes[i]

            # 遍历排在当前节点前面的所有节点 (时间必然 <= 当前节点)
            for j in range(i):
                prev_idx = key_nodes[j]

                # 链路建立条件: 互相有直接关联，且发生时间严格不同 (t_prev < t_curr)
                if associated[prev_idx][curr_idx] and nodes[prev_idx][2] < nodes[curr_idx][2]:
                    dp[i] = max(dp[i], dp[j] + nodes[curr_idx][4])

            # 更新全局最大值
            max_total_users = max(max_total_users, dp[i])

        # 输出当前测试用例的结果
        print(max_total_users)


if __name__ == '__main__':
    # ================= 本地测试用例区 =================
    # 使用 io.StringIO 模拟系统的标准输入流 sys.stdin，方便本地验证
    import io

    test_input = """
3 1 500
0 0 10 100 50
1 0 20 100 50
0 1 30 100 50
4 1 150
0 0 10 100 10
1 0 20 100 10
5 5 10 200 100
5 6 30 200 100
"""
    # 替换系统标准输入，仅用于本地测试。提交代码时保留原逻辑即可。
    sys.stdin = io.StringIO(test_input.strip())

    # 预期第一组输出 0 (无关键节点)，第二组输出 200
    solve()