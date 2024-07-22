import datetime
import pandas as pd
import os
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl import load_workbook


def process_excel(file_path, theme_mapping, object_mapping):
    # 读取 Excel 文件
    df = pd.read_excel(file_path)

    # 统计修改前满足条件的数量
    before_count_theme = df[
        (df['疑似水军'] == 1) &
        (df['主题'] == '其他')
        ].shape[0]

    before_count_object = df[
        (df['疑似水军'] == 1) &
        (df['对象'] == '其他')
        ].shape[0]

    # 创建一个函数来检查文本是否包含任意关键词
    def contains_keyword(text, keywords):
        if isinstance(text, str):
            return any(keyword in text for keyword in keywords)
        return False

    # 根据条件和关键词对应表更新主题
    for key, value in theme_mapping.items():
        mask = (
                (df['疑似水军'] == 1) &
                (df['主题'] == '其他') &
                (df['eda_text'].apply(contains_keyword, keywords=value))
        )
        df.loc[mask, '主题'] = key

    # 根据条件和关键词对应表更新对象
    for key, value in object_mapping.items():
        mask = (
                (df['疑似水军'] == 1) &
                (df['对象'] == '其他') &
                (df['eda_text'].apply(contains_keyword, keywords=value))
        )
        df.loc[mask, '对象'] = key

    # 统计修改后满足条件的数量
    after_count_theme = df[
        (df['疑似水军'] == 1) &
        (df['主题'] == '其他')
        ].shape[0]

    after_count_object = df[
        (df['疑似水军'] == 1) &
        (df['对象'] == '其他')
        ].shape[0]

    # 获取当前日期和时间，格式化时间戳
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y%m%d_%H%M")

    # 生成新文件名并保存在原文件夹中
    new_file_name = f"updated_{formatted_time}_油罐车-筛选.xlsx"
    new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

    # 保存到新文件
    df.to_excel(new_file_path, index=False)

    # 使用 openpyxl 读取新文件并进行列宽和隐藏列设置

    workbook = load_workbook(new_file_path)
    sheet = workbook.active

    # 隐藏列, 按列字母顺序隐藏，比如隐藏C、D列
    columns_to_hide = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for col in columns_to_hide:
        sheet.column_dimensions[col].hidden = True

    # 设置列宽，例如设置 A 列宽为 20，B 列宽为 30
    column_widths = {'I': 70}
    for col, width in column_widths.items():
        sheet.column_dimensions[col].width = width

    # 添加筛选功能，设置筛选的范围
    sheet.auto_filter.ref = sheet.dimensions

    # 冻结首行
    sheet.freeze_panes = 'A2'

    # 设置数据验证
    themes = [
        "暴力恐怖", "崇洋媚外", "黄谣色情", "群体对立", "辱骂攻击",
        "煽动仇富情绪", "煽动民族主义情绪", "煽动仇官情绪", "恶意谐音梗",
        "其他", "背景后台"
    ]
    objects = [
        "官方", "个人", "群体", "品牌", "组织", "其他", "国家民族"
    ]

    # 为 L 列设置数据验证
    dv_theme = DataValidation(
        type="list",
        formula1='"{}"'.format(",".join(themes)),
        allow_blank=True,
        showErrorMessage=True,
        showDropDown=True
    )
    dv_theme.add('L2:L10001')  # 整列验证，直到 Excel 的最大行数
    sheet.add_data_validation(dv_theme)

    # 为 M 列设置数据验证
    dv_object = DataValidation(
        type="list",
        formula1='"{}"'.format(",".join(objects)),
        allow_blank=True,
        showErrorMessage=True,
        showDropDown=True
    )
    dv_object.add('M2:M10001')  # 整列验证，直到 Excel 的最大行数
    sheet.add_data_validation(dv_object)

    # 保存最终修改的文件
    workbook.save(new_file_path)

    print(f"处理完成。新文件保存为: {new_file_path}")
    print(f"修改前满足条件的数量 (主题为其他): {before_count_theme}")
    print(f"修改后满足条件的数量 (主题为其他): {after_count_theme}")
    print(f"修改前满足条件的数量 (对象为其他): {before_count_object}")
    print(f"修改后满足条件的数量 (对象为其他): {after_count_object}")


# 定义主题对应的关键词
theme_mapping = {
    '暴力恐怖': ['自杀', '杀人', '毙了'],
    '崇洋媚外': ['移民', '润', '出国'],
    '黄谣色情': [],
    '群体对立': [],
    '辱骂攻击': ['枪毙', '死刑', '无期', '妈的', '判刑'],
    '煽动仇富情绪': ['资本', '富人'],
    '煽动民族主义情绪': ['外部', '势力'],
    '煽动仇官情绪': ['监管', '监督', '管理部门', '监督管理', '管理局', '成本太低', '成本低'],
    '恶意谐音梗': [],
    '背景后台': ['后台'],
    '其他': []
}

# 定义对象对应的关键词
object_mapping = {
    '官方': ['监管', '监督', '管理部门', '监督管理', '管理局', '法律', '部门', '电瓶车', '电动车', '公信力',
             '电动自行车', '腐败'],
    '个人': ['司马南', '司马', '责任人', '董事长', '领导', '当事人', '司机'],
    '群体': ['央企', '国企', '富人', '公司', '1450', '水军', '中字头', '企业'],
    '品牌': ['中储粮', '品牌', '国货', '商家', '鲁花', '中粮'],
    '组织': ['外资'],
    '国家民族': ['共产党', '外部', '势力', '美帝', '中国人', '美国'],
    '其他': []
}

# 使用示例，传入分类类别对应的关键词
file_path = "C:/Users/yuhuo/Documents/Code/pythonProject0619/src/0717/油罐车-筛选.xlsx"
process_excel(file_path, theme_mapping, object_mapping)
