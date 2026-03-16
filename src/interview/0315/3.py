"""
2
6
RURDLD
0 0
3
UDL
2 0
"""
import sys


def solve():
    # 使用 sys.stdin.read().split() 实现极致的 I/O 速度，应对大规模数据
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1
    out = []

    for _ in range(T):
        n = int(input_data[idx])
        s = input_data[idx + 1]
        target_x = int(input_data[idx + 2])
        target_y = int(input_data[idx + 3])
        idx += 4

        # 1. 计算一字不删情况下的原始终点坐标
        total_x, total_y = 0, 0
        for char in s:
            if char == 'U':
                total_y += 1
            elif char == 'D':
                total_y -= 1
            elif char == 'L':
                total_x -= 1
            elif char == 'R':
                total_x += 1

        # 2. 计算我们需要剔除的“目标差值向量”
        dx = total_x - target_x
        dy = total_y - target_y

        # 特判：如果一开始就已经正好落在目标点，一刀都不用切，答案为 0
        if dx == 0 and dy == 0:
            out.append("0")
            continue

        # 3. 前缀和 + 哈希表寻找最短匹配子串
        # 字典 pos_map 存储： (x坐标, y坐标) -> 达到该坐标的最新索引
        # 初始化起点 (0, 0) 的索引为 0
        pos_map = {(0, 0): 0}

        cx, cy = 0, 0
        min_len = float('inf')

        for i, char in enumerate(s, 1):
            # 更新当前的前缀坐标
            if char == 'U':
                cy += 1
            elif char == 'D':
                cy -= 1
            elif char == 'L':
                cx -= 1
            elif char == 'R':
                cx += 1

            # 我们想找的前置坐标
            target_prev_x = cx - dx
            target_prev_y = cy - dy

            # 如果在之前的历史轨迹中见过这个坐标，说明它们之间的那段子串正好符合要求
            if (target_prev_x, target_prev_y) in pos_map:
                current_len = i - pos_map[(target_prev_x, target_prev_y)]
                if current_len < min_len:
                    min_len = current_len

            # 更新当前坐标在哈希表中的最新索引
            # 注意：我们想要的是最短子串，所以 i - pos_map[xxx] 越小越好。
            # 因此这里如果同一坐标出现多次，直接无脑用更大的索引 i 覆盖旧的即可。
            pos_map[(cx, cy)] = i

        # 4. 判断并输出结果
        if min_len == float('inf'):
            out.append("-1")
        else:
            out.append(str(min_len))

    # 集中输出
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    solve()