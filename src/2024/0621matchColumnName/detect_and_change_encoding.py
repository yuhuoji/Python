import chardet
import pandas as pd


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']


def read_csv_with_encoding(file_path, encoding):
    with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
        return pd.read_csv(f)


def modify_encoding(input_file, output_file, new_encoding):
    # 检测当前文件的编码
    current_encoding = detect_encoding(input_file)

    # 读取原始文件
    df = read_csv_with_encoding(input_file, current_encoding)

    # 保存为新编码的文件
    df.to_csv(output_file, index=False, encoding=new_encoding)


file_path1 = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/cyber_star_info.csv'
file_path2 = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/cyber_star_info_backup.csv'
print(detect_encoding(file_path1))
print(detect_encoding(file_path2))

# 示例用法
input_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/cyber_star_info_backup.csv'
output_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/updated_cyber_star_info_backup.csv'
new_encoding = 'GB2312'

# 修改编码
# modify_encoding(input_file, output_file, new_encoding)
# print(f"文件 {input_file} 的编码已修改为 {new_encoding}，保存为 {output_file}")
