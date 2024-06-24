import pandas as pd

# 读取CSV文件并返回DataFrame
def read_csv_with_encoding(file_path, encoding):
    with open(file_path, 'r', encoding=encoding, errors='ignore') as f:
        return pd.read_csv(f)

# 更新'是否为抖音'列的函数（优化版）
def update_douyin_column(user_account_file, cyber_star_info_file, backup_file):
    # 读取user_account_info.csv和cyber_star_info_backup.csv
    df_user = read_csv_with_encoding(user_account_file, 'GB2312')
    df_star_info = read_csv_with_encoding(cyber_star_info_file, 'GB2312')

    # 处理NaN值
    df_user['url'] = df_user['url'].fillna('')

    # 提取包含douyin的url对应的cyber_start_id
    douyin_cyber_start_ids = set(df_user[df_user['url'].str.contains('douyin')]['cyber_start_id'])

    # 使用set进行快速匹配
    df_star_info['是否为抖音'] = df_star_info['id'].isin(douyin_cyber_start_ids).map({True: '是', False: ''})

    # 保存更新后的cyber_star_info_backup.csv
    df_star_info.to_csv(backup_file, index=False, encoding='GB2312')


# 文件路径
user_account_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/user_account_info.csv'
cyber_star_info_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/cyber_star_info_backup.csv'
update_file = 'C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0621matchColumnName/updateddouyin_cyber_star_info_backup.csv'

# 更新'是否为抖音'列
update_douyin_column(user_account_file, cyber_star_info_file, update_file)
