from django.db import connection

# 构建 SQL 查询语句
sql_query = """
    SELECT
        IFNULL(dc.department_name, 'Total') AS base_name,
        IFNULL(cat.category_name, 'Total') AS category_name,
        IFNULL(lvl.level_name, 'Total') AS level_name,
        COALESCE(COUNT(tc.id), 0) AS count,
        SUM(tc.content_people_number) AS total_people,
        SUM(tc.content_duration) AS total_duration,
        SUM(tc.content_satisfaction) AS total_satisfaction
    FROM
        hr_department dc
    CROSS JOIN
        training_content_category cat
    CROSS JOIN
        training_content_level lvl
    LEFT JOIN
        training_content tc ON tc.content_part_id = dc.id
                            AND tc.content_category_id = cat.id
                            AND tc.content_level_id = lvl.id
    WHERE
        dc.department_name IS NOT NULL
    GROUP BY
        dc.department_name, cat.category_name, lvl.level_name
    WITH ROLLUP;
"""

# 执行 SQL 查询
with connection.cursor() as cursor:
    cursor.execute(sql_query)
    result = cursor.fetchall()

# 处理查询结果
for row in result:
    base_name = row[0]
    category_name = row[1]
    level_name = row[2]
    count = row[3]
    total_people = row[4]
    total_duration = row[5]
    total_satisfaction = row[6]
    # 在此处处理每行的结果数据，例如打印或存储到一个数据结构中
