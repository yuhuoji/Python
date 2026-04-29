"""
示例1
5
1 2 3 4 5

对应输出
11100

示例2
5
5 2 7 3 2

对应输出
10000
"""

import sys


class BinaryTrie:
    def __init__(self):
        self.ch = [[-1, -1]]

    def insert(self, x: int) -> None:
        p = 0
        for b in range(29, -1, -1):
            bit = (x >> b) & 1
            if self.ch[p][bit] == -1:
                self.ch[p][bit] = len(self.ch)
                self.ch.append([-1, -1])
            p = self.ch[p][bit]

    def max_xor(self, x: int) -> int:
        p = 0
        res = 0
        for b in range(29, -1, -1):
            bit = (x >> b) & 1
            want = bit ^ 1
            if self.ch[p][want] != -1:
                res |= 1 << b
                p = self.ch[p][want]
            else:
                p = self.ch[p][bit]
        return res


def solve() -> None:
    input = sys.stdin.readline
    n = int(input().strip())
    a = list(map(int, input().split()))

    max_a = max(a)
    trie = BinaryTrie()
    ans = ['0'] * n

    trie.insert(a[-1])
    for i in range(n - 2, -1, -1):
        if trie.max_xor(a[i]) >= max_a:
            ans[i] = '1'
        trie.insert(a[i])

    print(''.join(ans))


if __name__ == "__main__":
    solve()
