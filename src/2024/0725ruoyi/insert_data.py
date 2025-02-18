import random
import mysql.connector

# 数据库连接配置
config = {
    'user': 'root',  # 替换为你的 MySQL 用户名
    'password': 'niyifei',  # 替换为你的 MySQL 密码
    'host': 'localhost',
    'database': 'ry',  # 替换为你的数据库名
}

# 创建数据库连接
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# 设置随机数据生成的数量
num_records = 1000  # 你可以修改这个值以设置数据量

# 随机数据内容
names = ['Alice', 'Bob', 'Charlie', 'Daisy', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack']
accounts = ['@alice', '@bob', '@charlie', '@daisy', '@eve', '@frank', '@grace', '@hannah', '@ian', '@jack']
categories = ['Society', 'Lifestyle', 'Sports', 'Arts', 'Other']
features = ['Explicit', 'Implicit']
statuses = ['Active', 'Inactive']

# 生成插入语句并执行
for _ in range(num_records):
    name = random.choice(names)
    account = f'@{name.lower()}'  # 将用户名转换为小写并加上 '@'
    category = random.choice(categories)
    feature = random.choice(features)
    fans = random.randint(1000, 50000)  # 随机粉丝数
    works = random.randint(1, 200)  # 随机作品数
    status = random.choice(statuses)

    # 插入数据的 SQL 语句
    insert_statement = ("INSERT INTO cyber_star (cyber_star_name, account, category, "
                        "associated_feature, fans, works, status) VALUES (%s, %s, %s, %s, %s, %s, %s)")
    data = (name, account, category, feature, fans, works, status)

    # 执行插入操作
    cursor.execute(insert_statement, data)

# 提交事务
connection.commit()

# 关闭游标和连接
cursor.close()
connection.close()

print(f"成功插入 {num_records} 条记录")
