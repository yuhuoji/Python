import sys

"""
3
5 3
1 2 3 4 5
0 7 5
3 2
10 -5 7
3 2
6 3
0 1 2 3 4 5
6 4 7
"""


def function():
    lines = sys.stdin.read().split()
    if not lines:
        return
    ptr = 0
    T_str = lines[ptr]
    ptr += 1
    T = int(T_str)

    results = []

    MAX_BIT = 18
    MAX_VAL = 1 << MAX_BIT

    for _ in range(T):
        n = int(lines[ptr])
        q = int(lines[ptr + 1])
        ptr += 2

        f = [0] * MAX_VAL

        for i in range(1, n + 1):
            f[i] = int(lines[ptr])
            ptr += 1

        for i in range(MAX_BIT):
            for mask in range(MAX_VAL):
                if mask & (1 << i):
                    f[mask] += f[mask ^ (1 << i)]

        for _ in range(q):
            x = int(lines[ptr])
            ptr += 1
            if x > MAX_VAL:
                results.append(str(f[MAX_VAL - 1]))
            else:
                results.append(str(f[x]))
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    function()