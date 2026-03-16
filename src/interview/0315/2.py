"""
20 10 3
4 5
9 2
15 6
"""
import sys


def solve():
    # 使用 sys.stdin.read().split() 进行超快速的 I/O 读入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    L = int(input_data[0])
    C = int(input_data[1])
    n = int(input_data[2])

    # stations 存储格式: (距离, 价格)
    # 核心技巧：把起点视作距离为0，充电价格为0的“超级充电站”
    stations = [(0, 0)]

    idx = 3
    for _ in range(n):
        d = int(input_data[idx])
        p = int(input_data[idx + 1])
        stations.append((d, p))
        idx += 2

    # 把终点视作距离为 L，充电价格为0的“终极目标”
    stations.append((L, 0))

    ans = 0
    curr = 0
    batt = 0  # 初始电量设为0，但在0号站可以免费充到满 (C)

    # 遍历直到到达终点（倒数第一个元素）
    while curr < len(stations) - 1:
        curr_d, curr_p = stations[curr]

        best_cheaper = -1
        min_price_idx = -1
        min_price = float('inf')

        nxt = curr + 1
        # 往后扫描所有在续航 C 范围内的充电站
        while nxt < len(stations) and stations[nxt][0] - curr_d <= C:
            p_nxt = stations[nxt][1]

            # 找到范围内第一个价格 <= 当前价格的站，立刻锁定
            if p_nxt <= curr_p:
                best_cheaper = nxt
                break

            # 如果找不到更便宜的，就记录范围内价格最便宜的站
            # (如果有多个相同的最低价，使用 <= 可以保证我们走到最远的那个)
            if p_nxt <= min_price:
                min_price = p_nxt
                min_price_idx = nxt

            nxt += 1

        # 验证是否连紧挨着的下一个站都够不着（无法到达目的地）
        if nxt == curr + 1 and stations[nxt][0] - curr_d > C:
            print(-1)
            return

        if best_cheaper != -1:
            # 策略1：范围内有更便宜的站，只需充电刚好够开到那个站即可
            target = best_cheaper
            dist = stations[target][0] - curr_d
            if batt < dist:
                ans += (dist - batt) * curr_p  # 只充缺失的电量
                batt = dist
            batt -= dist
            curr = target
        else:
            # 策略2：范围内全是更贵的站，在当前站直接充满，开往范围内最便宜的那个站
            target = min_price_idx
            ans += (C - batt) * curr_p  # 充到满
            batt = C
            dist = stations[target][0] - curr_d
            batt -= dist
            curr = target

    print(ans)


if __name__ == '__main__':
    solve()