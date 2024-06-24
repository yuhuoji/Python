import pandas as pd


def read_csv_with_encoding(file_path, encoding):
    with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
        return pd.read_csv(f)


def compare_csv_files(file1, file2):
    # 读取 CSV 文件
    df1 = read_csv_with_encoding(file1, 'GB2312')
    df2 = read_csv_with_encoding(file2, 'GB2312')

    # 检查两个文件是否有相同的列
    if set(df1.columns) != set(df2.columns):
        print("两个文件的列名不同", df1.columns, ", ", df2.columns)
        print("File1 columns:", df1.columns)
        print("File2 columns:", df2.columns)
        return

    # 比较文件行数是否相同
    if len(df1) != len(df2):
        print("两个文件的行数不同")
        print("File1 rows:", len(df1))
        print("File2 rows:", len(df2))
        return

    # 找出不同的列及其不同的行号
    different_columns = []
    diff_rows = {}
    for col in df1.columns:
        diff_rows[col] = []
        for idx in df1.index:
            if pd.isna(df1.at[idx, col]) and pd.isna(df2.at[idx, col]):
                continue  # 如果两个单元格都是空的，则跳过比较
            if df1.at[idx, col] != df2.at[idx, col]:
                if col not in different_columns:
                    different_columns.append(col)
                if idx not in diff_rows[col]:
                    diff_rows[col].append(idx)

    if len(different_columns) == 0:
        print("两个文件完全相同")
    elif len(different_columns) == 1:
        print(f"两个文件只有列 '{different_columns[0]}' 不同")
        # print(f"不同的行号: {diff_rows[different_columns[0]]}")
        print(f"不同的行号个数: {len(diff_rows[different_columns[0]])}")
    else:
        print(f"两个文件有多个不同的列: {different_columns}")
        for col in different_columns:
            print(f"列 '{col}' 不同的行号: {diff_rows[col]}")
            print(f"列 '{col}' 不同的行号个数: {len(diff_rows[col])}")


# 文件路径
file1 = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0624modify_column_value_by_mark_column/6.24updated_cyber_star_info.csv'
file2 = 'C:/Users/yuhuo/Documents/Document/6.17-21/6.21/cyber_star_info.csv'

# 比较两个 CSV 文件
compare_csv_files(file1, file2)
