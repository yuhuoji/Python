"""
2
2
??
5
A?B??
"""

import sys

MOD = 10**9 + 7


def solve() -> None:
    input = sys.stdin.readline
    t = int(input().strip())
    ans = []

    for _ in range(t):
        n = int(input().strip())
        s = input().strip()

        # dp_a: 当前处理到 i，且 s[i] 所在这一段长度为奇数，最后一个字符是 A 的方案数
        # dp_b: 当前处理到 i，且 s[i] 所在这一段长度为奇数，最后一个字符是 B 的方案数
        # ep_a: 当前处理到 i，且最后一个字符是 A，且这一段长度为偶数的方案数
        # ep_b: 当前处理到 i，且最后一个字符是 B，且这一段长度为偶数的方案数
        dp_a = dp_b = ep_a = ep_b = 0

        if s[0] in ("A", "?"):
            dp_a = 1
        if s[0] in ("B", "?"):
            dp_b = 1

        for i in range(1, n):
            ndp_a = ndp_b = nep_a = nep_b = 0

            if s[i] in ("A", "?"):
                # 接在 A 后面：奇 <-> 偶
                nep_a = (nep_a + dp_a) % MOD
                ndp_a = (ndp_a + ep_a) % MOD
                # 从 B 切换到 A：前一段必须已经是奇数长度
                ndp_a = (ndp_a + dp_b) % MOD

            if s[i] in ("B", "?"):
                # 接在 B 后面：奇 <-> 偶
                nep_b = (nep_b + dp_b) % MOD
                ndp_b = (ndp_b + ep_b) % MOD
                # 从 A 切换到 B：前一段必须已经是奇数长度
                ndp_b = (ndp_b + dp_a) % MOD

            dp_a, dp_b, ep_a, ep_b = ndp_a, ndp_b, nep_a, nep_b

        # 最后一段也必须是奇数长度
        ans.append(str((dp_a + dp_b) % MOD))

    print("\n".join(ans))


if __name__ == "__main__":
    solve()
