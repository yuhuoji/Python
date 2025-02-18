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

# SQL 清空表语句
truncate_statement = "TRUNCATE TABLE cyber_star;"

try:
    # 执行清空表操作
    cursor.execute(truncate_statement)

    # 提交事务（可选，TRUNCATE 会自动提交）
    # connection.commit()
    print("成功清空表中的所有数据，表结构保留")

except mysql.connector.Error as err:
    print(f"数据库错误: {err}")

finally:
    # 关闭游标和连接
    cursor.close()
    connection.close()