import sys

"""
3
1 4 7
"""
n = list(map(int, sys.stdin.readline().strip()))[0]
line = list(map(int, sys.stdin.readline().strip().split()))

# print(n, end="\n")
# for x in line:
#     print(x, end=" ")
ans = sum(line)
print(ans)
