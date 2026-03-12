import sys

"""
4
6 2
2 1
30 4
1000000000000 1

t
n m
"""


def function1(n, m) -> int:
    max_k = -1
    t_val = 1
    while True:
        cnt_odd = t_val * m
        min_odd_sum = 3 * cnt_odd
        if min_odd_sum > n:
            break
        rem = n - min_odd_sum
        if rem % 2 == 0:
            cnt_2 = rem // 2
            k = cnt_odd + cnt_2
            max_k = k
            break
        t_val += 1
    return max_k


def function2(n, m) -> int:
    min_odd = 3 * m
    if min_odd > n:
        return -1

    parity_n = n % 2
    parity_3m = (3 * m) % 2
    if parity_3m == parity_n:
        t = 1
    else:
        t = 2
        if 3 * m * t > n:
            return -1
    cnt_odd = t * m
    sum_odd = 3 * cnt_odd
    rem = n - sum_odd
    cnt_2 = rem // 2
    max_k = cnt_odd + cnt_2
    return max_k


def function():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    ptr = 1
    results = []
    for _ in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr+1] )
        ptr += 2
        min_sum = 3 * m
        if n < min_sum:
            results.append("-1")
            continue
        if (n % 2) == (m % 2):
            k = m + (n - 3 * m) // 2
            results.append((str(k)))
        else:
            best_k = -1
            if n >= 3 * (2 * m) and (n % 2 == 0):
                k2 = 2 * m + (n - 3 * (2 * m)) // 2
                best_k = k2
            results.append((str(best_k)))
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    function()
# lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
# ptr = 0
# t = int(lines[ptr])
# ptr += 1
# for _ in range(t):
#     n, m = map(int, lines[ptr].split())
#     ptr += 1
#     ans = function(n, m)
#     print(ans)
