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
    letters = ''.join(random.choice(string.digits) for _ in range(3))
    return f"MCN{letters}"

def generate_random_url():
    length = random.randint(3, 8)  # Random length between 3 and 8
    random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
    return f"www.{random_string}.com"

# 随机数据范围设置
countries = ['USA', 'CHN', 'IND', 'GBR', 'FRA']
categories = ['Tech', 'Media', 'Entertainment', 'Education', 'Finance']
statuses = ['Active', 'Inactive', 'Pending', 'Closed']
platforms = ['Bilibili', 'Douyin', 'Facebook', 'Kuaishou', 'News', 'TikTok', 'Twitter', 'Weibo', 'YouTube', 'Zhihu']
die_out_reasons = ['Low Performance', 'Regulation Issues', 'Market Changes', 'Financial Problems']

def insert_random_data(num_records):
    try:
        with connection.cursor() as cursor:
            # 禁用外键约束
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

            # 使用 TRUNCATE TABLE 清空表并重置 AUTO_INCREMENT
            truncate_sql = "TRUNCATE TABLE mcn_organ"
            cursor.execute(truncate_sql)

            # 启用外键约束
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

            # 插入新的随机数据
            for _ in range(num_records):
                name = generate_random_name()
                url = generate_random_url()
                fans = random.randint(1000, 1000000)
                country = random.choice(countries)
                remark = 'This is a remark'
                category = random.choice(categories)
                head_img = f'http://images.com/{random.randint(1, 100)}.jpg'
                status = random.choice(statuses)
                capital = random.randint(10000, 1000000)
                signing_scale = random.randint(1, 100)
                account_num = random.randint(1, 1000)
                platform = random.choice(platforms)
                die_out_reason = random.choice(die_out_reasons)
                mark = 'Additional remarks here.'

                sql = """  
                INSERT INTO mcn_organ (name, url, fans, country, remark, category, head_img, status, capital, signing_scale, account_num, platform, die_out_reason, mark)  
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)  
                """
                cursor.execute(sql, (
                    name, url, fans, country, remark, category, head_img, status, capital, signing_scale, account_num,
                    platform, die_out_reason, mark))

        connection.commit()
        print(f"Inserted {num_records} records into the database.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

# 设置要插入的数据量
num_records_to_insert = 1000

# 调用函数插入指定数量的随机数据
insert_random_data(num_records_to_insert)