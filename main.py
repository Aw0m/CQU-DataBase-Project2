from db import Database

if __name__ == '__main__':
    # 创建/选择数据库 如果没有该数据库则直接创建
    db = Database("db_test")

    # 创建表
    db.create_table(table_name="Employee", pr_key="E_id", field=['E_name', 'E_number', 'E_sex', 'E_tel'])

    # 插入
    db.insert(table_name="Employee", pr_key=10000, field=["张三", '22', 'male', 15266668888])

    # 查找（找到了）
    print(db.select(table_name="Employee", pr_key=10000))

    # 更新
    db.update(table_name="Employee", pr_key=10000, field=["张三", '23', 'male', 15266668888])

    # 查找（找到了）
    print(db.select(table_name="Employee", pr_key=10000))

    # 删除
    db.delete(table_name="Employee", pr_key=10000)

    # 查找（找不到了）
    print(db.select(table_name="Employee", pr_key=10000))

    db.close()

