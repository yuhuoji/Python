import sys
import heapq
"""
1
4 4
1 2
2 2
2 3
4 5
2 3 5 6

1
3 2
1 1
2 2
3 3
1 3
"""

def solve():
    # 读取所有输入数据以提高 I/O 效率
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    T = int(input_data[0])
    idx = 1

    for _ in range(T):
        n = int(input_data[idx])
        m = int(input_data[idx + 1])
        idx += 2

        contents = []
        for _ in range(n):
            l = int(input_data[idx])
            r = int(input_data[idx + 1])
            contents.append((l, r))
            idx += 2

        slots = []
        for _ in range(m):
            slots.append(int(input_data[idx]))
            idx += 1

        # 1. 按照左端点从小到大排序内容区间
        contents.sort(key=lambda x: x[0])
        # 2. 按照热度值从小到大排序推荐位
        slots.sort()

        min_heap = []
        content_idx = 0
        match_count = 0

        # 3. 遍历每一个推荐位
        for s in slots:
            # 将所有左端点 <= 当前推荐位热度的内容上限 r 加入最小堆
            while content_idx < n and contents[content_idx][0] <= s:
                heapq.heappush(min_heap, contents[content_idx][1])
                content_idx += 1

            # 清理堆中那些上限已经 < 当前推荐位热度的内容（它们已经无法被后续匹配）
            while min_heap and min_heap[0] < s:
                heapq.heappop(min_heap)

            # 如果堆不为空，取出上限最小的内容与当前推荐位匹配
            if min_heap:
                heapq.heappop(min_heap)
                match_count += 1

        print(match_count)


if __name__ == '__main__':
    solve()

