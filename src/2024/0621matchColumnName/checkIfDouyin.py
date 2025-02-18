import pandas as pd


# 读取CSV文件并返回DataFrame
def read_csv_with_encoding(file_path, encoding):
    with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
        return pd.read_csv(f)


# 更新列的函数
def update_csv_file(file_path, output_path):
    # 读取CSV文件
    df = read_csv_with_encoding(file_path, 'GB2312')

    # 遍历每一行，根据条件修改列值
    for idx, row in df.iterrows():
        if row['是否为抖音'] == '是':
            if row['显性=1，隐性=2'] == 1:
                df.at[idx, 'association_feature'] = '显性'
            elif row['显性=1，隐性=2'] == 2:
                df.at[idx, 'association_feature'] = '隐性'

    # 删除指定的列
    df = df.drop(columns=['显性=1，隐性=2', '是否为抖音'])

    # 格式化输出，确保所有行的行距都一样
    with open(output_path, 'w', encoding='GB2312', newline='') as f:
        df.to_csv(f, index=False, line_terminator='\n', encoding='GB2312')

    # 保存更新后的CSV文件
    df.to_csv(output_path, index=False, encoding='GB2312')


# 文件路径
input_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0624modify_column_value_by_mark_column/cyber_star_info_backup.csv'
output_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0624modify_column_value_by_mark_column/updated_cyber_star_info_backup.csv'

# 更新CSV文件
update_csv_file(input_file, output_file)
