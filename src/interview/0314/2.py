"""
2 5
1
2
3
4
5
"""
# import sys
# MOD = 10**9 + 7
#
# def main():
#     data = sys.stdin.read().split()
#     ptr = 0
#     k = int(data[ptr])
#     ptr +=1
#     q = int(data[ptr])
#     ptr +=1
#
#     qs = list(map(int, data[ptr:ptr+q]))
#     need = set(qs)
#     mx = max(qs)
#
#     window = [1]*k
#     s = k % MOD
#     ans = {}
#
#     for i in range(1, mx+1):
#         if i <= k:
#             v = 1
#         else:
#             v = s % MOD
#             s = (s + v - window[0]) % MOD
#             window.append(v)
#             window.pop(0)
#         if i in need:
#             ans[i] = v
#
#     for x in qs:
#         print(ans[x]%MOD)
#
# if __name__ == '__main__':
#     main()

import sys
MOD = 10**9 + 7

def main():
    data = sys.stdin.read().split()
    ptr = 0
    k = int(data[ptr])
    ptr +=1
    q = int(data[ptr])
    ptr +=1

    qs = list(map(int, data[ptr:ptr+q]))
    need = set(qs)
    mx = max(qs)

    window = [1]*k
    s = k % MOD
    ans = {}

    for i in range(1, mx+1):
        if i <= k:
            v = 1
        else:
            v = s % MOD
            s = (s + v - window[0]) % MOD
            window.append(v)
            window.pop(0)
        if i in need:
            ans[i] = v

    for x in qs:
        print(ans[x]%MOD)

if __name__ == '__main__':
    main()