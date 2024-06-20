import pandas as pd

# 读取第一个 CSV 文件
df1 = pd.read_csv('C:/Users/yuhuo/Documents/Document/6.17-21/6.20/图谱人物数据.csv')

# 读取第二个 CSV 文件
df2 = pd.read_csv('C:/Users/yuhuo/Documents/Document/6.17-21/6.20/图谱人物数据-原数据 - 副本.csv')

# 比较两个文件的指定列，假设要比较 'institution' 列
column = 'institution'

# 找出不同的行的行号
different_rows = []
for row in range(len(df1)):
    cell1 = str(df1.at[row, column]).strip()
    cell2 = str(df2.at[row, column]).strip()
    if cell1 != cell2 and not (cell1 == '' and cell2 == ''):
        different_rows.append((row, cell1, cell2))

# 输出不同的行号和两个单元格的内容
print("不一样的行号和对应的单元格内容:")
for row, cell1, cell2 in different_rows:
    print(f"行号: {row}, 文件1的内容: {cell1}, 文件2的内容: {cell2}")
