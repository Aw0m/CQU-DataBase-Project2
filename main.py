from db import Database

if __name__ == '__main__':
    # 创建/选择数据库 如果没有该数据库则直接创建
    db = Database("db4")

    # 创建表
    db.create_table(table_name="new_table1", pr_key="t1_pr", field=['col1', 'col2', 'col3'])

    # 插入（错误！因为字段数量不匹配）
    db.insert(table_name="new_table1", pr_key=71, field=["123", '423', '12321', 123])

    # 插入
    db.insert(table_name="new_table1", pr_key=71, field=["123", '423', '12321'])

    # 失败，因为已经有相同pr_key的已经插入
    db.insert(table_name="new_table1", pr_key=71, field=["123", '423', '12321'])

    # 查找（找到了）
    print(db.select(table_name="new_table1", pr_key=71))

    # 更新（错误！因为字段数量不匹配）
    db.update(table_name="new_table1", pr_key=71, field=[1, 1, 1, 4])

    # 更新
    db.update(table_name="new_table1", pr_key=71, field=[1, 1, 1])

    # 查找
    print(db.select(table_name="new_table1", pr_key=71))

    # 查找 （没找到）
    print(db.select(table_name="new_table1", pr_key=12371))

    db.close()

