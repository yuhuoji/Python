import sys

"""
3 2
1 2
2 3
3
1 1 5
2 3 10
3 2 1
"""
lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]  # 关键ACM读取输入
ptr = 0
n, m = map(int, lines[ptr].split())
print("n = ", n)
print("m = ", m)

sys.stdin.read()