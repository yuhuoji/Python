"""
5 4
1 100 20 5
2 100 20 3
1 120 10 8
3 100 20 4
2 110 18 6
1
2
3
5
"""
import sys

def solve():
    # 快速读取所有输入数据，按空白字符分割为列表
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    q = int(input_data[1])

    # 记录每个主播最优的一条直播内容
    # 字典格式：主播id u -> ((排序元组), 原始编号id)
    best_for_streamer = {}

    idx = 2
    for i in range(1, n + 1):
        u = int(input_data[idx])
        a = int(input_data[idx + 1])
        b = int(input_data[idx + 2])
        t = int(input_data[idx + 3])
        idx += 4

        # 构造多关键字排序元组
        # 规则1：点赞数越多越优 -> 取相反数 -a (让原本大的变成小的)
        # 规则2：评论数越多越优 -> 取相反数 -b
        # 规则3：发布时间越早越优 -> 时间越小越早，直接用 t
        # 规则4：编号越小越优 -> 直接用 i
        # Python 的 tuple 默认从小到大依次比较，所以我们将越优的条件转换为越小的值
        sort_key = (-a, -b, t, i)

        # 如果该主播还没有记录，或者当前内容的排序元组更小（更优）
        if u not in best_for_streamer or sort_key < best_for_streamer[u][0]:
            best_for_streamer[u] = (sort_key, i)

    # 提取所有成功上榜（去重后保留）的直播内容，并进行最终排序
    # 因为 sort_key 已经按照“越优的值越小”设计，直接用 sort() 升序即可
    leaderboard = list(best_for_streamer.values())
    leaderboard.sort()

    # 构建一个答案数组，ans[id] 存 id 对应的最终排名，被淘汰的默认为 0
    ans = [0] * (n + 1)
    for rank, (key, original_id) in enumerate(leaderboard, 1):
        ans[original_id] = rank

    # 处理 q 次查询
    out = []
    for _ in range(q):
        query_id = int(input_data[idx])
        idx += 1
        out.append(str(ans[query_id]))

    # 快速输出所有结果
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    solve()