"""
示例1输入：
4,[2,2,2,0],0

示例1输出：
[1,0,3,1,2]

示例2输入：
3,[0,1,1],2

示例2输出：
[1,-1,0,1]
"""

import sys
import re


def solve():
    s = sys.stdin.read().strip()
    nums = list(map(int, re.findall(r"-?\d+", s)))

    n = nums[0]
    a = nums[1:1 + n]
    k = nums[1 + n]

    # 总计数，只需要统计 0 ~ n
    total_cnt = [0] * (n + 1)
    for x in a:
        if 0 <= x <= n:
            total_cnt[x] += 1

    # 可调整位置的计数
    adjustable_cnt = total_cnt[:]

    fixed_value = -1
    if k != 0:
        fixed_value = a[k - 1]
        if 0 <= fixed_value <= n:
            adjustable_cnt[fixed_value] -= 1

    ans = []
    missing = 0

    for mex in range(n + 1):
        if mex > 0:
            prev = mex - 1
            if total_cnt[prev] == 0:
                missing += 1

        if fixed_value == mex:
            ans.append(-1)
        else:
            ans.append(max(missing, adjustable_cnt[mex]))

    print("[" + ",".join(map(str, ans)) + "]")


if __name__ == "__main__":
    solve()