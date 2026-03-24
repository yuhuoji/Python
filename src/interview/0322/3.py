import sys

"""
5 2
0 2 -5 4 -3
"""
def solve():
    # 使用 sys.stdin.read 一次性读取，极大提升 IO 速度
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2:2 + n]]

    # 构建前缀和数组 P
    # P 长度为 n + 1，P[0] = 0
    P = [0] * (n + 1)
    for i in range(n):
        P[i + 1] = P[i] + a[i]

    # 计算线段树叶子节点需要的容量 (2的幂次)
    m = n + 1
    SZ = 1
    while SZ < m:
        SZ *= 2

    # 初始化非递归线段树数组 (存储区间最大值)
    # 空间为 2 * SZ，初始极小值
    tree = [-float('inf')] * (2 * SZ)

    # 填充叶子节点
    for i in range(m):
        tree[SZ + i] = P[i]

    # 自底向上建树
    for i in range(SZ - 1, 0, -1):
        tree[i] = max(tree[i * 2], tree[i * 2 + 1])

    def query_first(L, R, val, is_gt):
        """
        在线段树中查询区间 [L, R] 内第一个 大于/大于等于 val 的索引
        is_gt 为 True 则查 > val，为 False 则查 >= val
        """
        L += SZ
        R += SZ
        left_nodes = []
        right_nodes = []

        # 提取覆盖区间 [L, R] 的所有节点
        while L <= R:
            if L % 2 == 1:
                left_nodes.append(L)
                L += 1
            if R % 2 == 0:
                right_nodes.append(R)
                R -= 1
            L //= 2
            R //= 2

        # 按照原数组中从左到右的顺序拼接节点
        for node in left_nodes + right_nodes[::-1]:
            condition_met = (tree[node] > val) if is_gt else (tree[node] >= val)

            # 如果当前子树的最大值满足条件，说明目标一定在这棵子树里
            if condition_met:
                # 不断向下寻找最左侧的满足条件的叶子节点
                while node < SZ:
                    left_child_met = (tree[node * 2] > val) if is_gt else (tree[node * 2] >= val)
                    if left_child_met:
                        node = node * 2
                    else:
                        node = node * 2 + 1
                return node - SZ

        return -1  # 未找到

    total_valid = 0

    # 遍历所有可能的左端点 l
    for l in range(1, n + 1):
        target = P[l - 1] + k

        # 寻找第一个 >= target 的位置
        idx1 = query_first(l, n, target, False)

        # 如果找不到，或者找到的第一个大等于的数并不等于 target，说明该 l 无解
        if idx1 == -1 or P[idx1] != target:
            continue

        # 寻找第一个 > target 的位置
        idx2 = query_first(l, n, target, True)

        # 如果没有 > target 的元素，说明一直到结尾都满足恰好等于 target
        if idx2 == -1:
            idx2 = n + 1

        # 累加合法右端点 r 的数量
        total_valid += (idx2 - idx1)

    print(total_valid)


if __name__ == '__main__':
    solve()