import random
import string

import pymysql

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
    numbers = ''.join(random.choice(string.digits) for _ in range(8))
    return f"Fan{numbers}"

# 随机数据范围设置
descriptions = ['Content creator', 'Influencer', 'Artist', 'Gamer', 'Musician']
platforms = ['Bilibili', 'Douyin', 'Facebook', 'Kuaishou', 'News', 'TikTok', 'Twitter', 'Weibo', 'YouTube', 'Zhihu']
statuses = ['Active', 'Inactive', 'Suspended', 'Pending']

def insert_random_account_data(num_records):
    try:
        with connection.cursor() as cursor:
            # 获取所有 mcn_organ_id 和 cyber_star_id
            cursor.execute("SELECT mcn_organ_id FROM mcn_organ")
            mcn_organ_ids = [row['mcn_organ_id'] for row in cursor.fetchall()]

            cursor.execute("SELECT cyber_star_id FROM cyber_star")
            cyber_star_ids = [row['cyber_star_id'] for row in cursor.fetchall()]

            if not mcn_organ_ids or not cyber_star_ids:
                print("No MCN organizations or cyber stars found. Ensure mcn_organ and cyber_star tables have data.")
                return

            for _ in range(num_records):
                user_name = generate_random_name()
                user_id = random.randint(1, 100000)
                mcn_organ_id = random.choice(mcn_organ_ids)
                cyber_star_id = random.choice(cyber_star_ids)
                description = random.choice(descriptions)
                homepage_url = f"http://homepage.com/{random.randint(1, 1000)}"
                content_source = "Generated Content"
                fan_count = str(random.randint(1000, 1000000))
                work_title = f"Work {random.randint(1, 20)}"
                like_count = random.randint(0, 500000)
                social_platform = random.choice(platforms)
                category = random.choice(['Tech', 'Lifestyle', 'Education'])
                profile_image = f"http://images.com/profile/{random.randint(1, 500)}.jpg"
                status = random.choice(statuses)
                capital_value = str(random.randint(5000, 100000))
                signed_contracts = str(random.randint(1, 50))
                account_number = str(random.randint(1, 100))
                platform = random.choice(platforms)

                sql = """  
                INSERT INTO account (user_id, user_name, mcn_organ_id, cyber_star_id, description, homepage_url, content_source, fan_count, work_titles, like_count, social_platform, category, profile_image, status, capital_value, signed_contracts, account_number, platform)  
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)  
                """
                cursor.execute(sql, (user_id, user_name, mcn_organ_id, cyber_star_id, description, homepage_url, content_source, fan_count, work_title, like_count, social_platform, category, profile_image, status, capital_value, signed_contracts, account_number, platform))

        connection.commit()
        print(f"Inserted {num_records} records into the account table.")
    except Exception as e:
        print(f"An error occurred while inserting data: {e}")
    finally:
        connection.close()

# 设置要插入的数据量
num_records_to_insert = 100000

# 调用函数插入指定数量的随机数据
insert_random_account_data(num_records_to_insert)