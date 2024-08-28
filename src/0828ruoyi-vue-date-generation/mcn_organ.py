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

# 随机数据范围设置
names = ['Alpha Media', 'Beta Group', 'Gamma Entertainment', 'Delta Productions', 'Epsilon Studios']
urls = ['www.alpha.com', 'www.beta.com', 'www.gamma.com', 'www.delta.com', 'www.epsilon.com']
countries = ['USA', 'CHN', 'IND', 'GBR', 'FRA']
categories = ['Tech', 'Media', 'Entertainment', 'Education', 'Finance']
statuses = ['Active', 'Inactive', 'Pending', 'Closed']
platforms = ['YouTube', 'Instagram', 'TikTok', 'Twitter', 'Facebook']
die_out_reasons = ['Low Performance', 'Regulation Issues', 'Market Changes', 'Financial Problems']

def insert_random_data(num_records):
    try:
        with connection.cursor() as cursor:
            # 使用 TRUNCATE TABLE 清空表并重置 AUTO_INCREMENT
            truncate_sql = "TRUNCATE TABLE mcn_organ"
            cursor.execute(truncate_sql)

            # 插入新的随机数据
            for _ in range(num_records):
                name = random.choice(names)
                url = random.choice(urls)
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
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

# 调用函数插入指定数量的随机数据
insert_random_data(1000)