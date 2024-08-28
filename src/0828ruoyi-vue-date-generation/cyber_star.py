import random
import pymysql
import string

# 连接到 MySQL 数据库
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='ry-vue',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def generate_random_name():
    letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    return f"Star {letters}"

# 随机数据范围设置
statuses = ['Active', 'Inactive', 'Pending', 'Closed']
die_out_reasons = ['Low Performance', 'Regulation Issues', 'Market Changes', 'Financial Problems']

def insert_random_data(num_records):
    try:
        with connection.cursor() as cursor:
            # 获取所有 mcn_organ_id
            cursor.execute("SELECT mcn_organ_id FROM mcn_organ")
            mcn_organ_ids = [row['mcn_organ_id'] for row in cursor.fetchall()]

            if not mcn_organ_ids:
                print("No MCN organizations found. Please ensure mcn_organ table has data.")
                return

            # 使用 TRUNCATE TABLE 清空表并重置 AUTO_INCREMENT
            truncate_sql = "TRUNCATE TABLE cyber_star"
            cursor.execute(truncate_sql)

            # 插入新的随机数据
            for _ in range(num_records):
                name = generate_random_name()
                mcn_organ_id = random.choice(mcn_organ_ids)
                remark = 'This is a remark'
                status = random.choice(statuses)
                die_out_reason = random.choice(die_out_reasons)
                mark = 'Additional remarks here.'

                sql = """  
                INSERT INTO cyber_star (name, mcn_organ_id, remark, status, die_out_reason, mark)  
                VALUES (%s, %s, %s, %s, %s, %s)  
                """
                cursor.execute(sql, (
                    name, mcn_organ_id, remark, status, die_out_reason, mark))

        connection.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

# 调用函数插入指定数量的随机数据
insert_random_data(1000)