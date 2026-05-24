"""
示例输入：
NiuNiu NiuMei NiuNeng

示例输出：
['NiuNiu', 'NiuMei', 'NiuNeng']
"""

import sys

# 读取所有输入内容
s = sys.stdin.read().strip()

# 按空格切分成列表
ans = s.split()

# 输出封装后的列表
print(ans)