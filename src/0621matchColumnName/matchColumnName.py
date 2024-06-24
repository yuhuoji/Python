import pandas as pd
import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']


def read_csv_with_encoding(file_path, encoding):
    with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
        return pd.read_csv(f)


def update_c_file(A_file, B_file, C_file, output_file):
    # 检测文件编码
    B_encoding = detect_encoding(B_file)
    C_encoding = detect_encoding(C_file)

    print(f"B file encoding: {B_encoding}")
    print(f"C file encoding: {C_encoding}")

    # 读取 A 文件
    df_A = pd.read_excel(A_file)

    # 读取 B 文件，处理编码错误
    df_B = read_csv_with_encoding(B_file, B_encoding)

    # 读取 C 文件，处理编码错误
    df_C = read_csv_with_encoding(C_file, C_encoding)

    # 打印 B 文件和 C 文件的列名
    print("B file columns:", df_B.columns)
    print("C file columns:", df_C.columns)

    # 提取 A 文件中的抖音号名称和关联MCN
    douyin_names = df_A['抖音号名称']
    mcn_names = df_A['关联MCN']

    # 创建一个字典用于存储 B 文件中匹配到的 cyber_start_id 和 mcn_organ_id
    id_map = {}

    for index, row in df_B.iterrows():
        if row['user_name'] in douyin_names.values and row['mcn_organ_name'] in mcn_names.values:
            id_map[(row['user_name'], row['mcn_organ_name'])] = (row['cyber_start_id'], row['mcn_organ_id'])

    # 更新 C 文件
    for index, row in df_C.iterrows():
        for key, value in id_map.items():
            if row['id'] == value[0] and row['mcn_organ_id'] == value[1]:
                df_C.at[index, '显性=1，隐性=2'] = 1

    # 保存更新后的 C 文件
    df_C.to_csv(output_file, index=False, encoding='utf-8')


# 文件路径
A_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/新抖-全部网红20240108035637.xlsx'
B_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/user_account_info.csv'
C_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/cyber_star_info.csv'
output_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/updated_cyber_star_info.csv'

# 更新 C 文件
update_c_file(A_file, B_file, C_file, output_file)
