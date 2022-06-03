import xlwings as xw


class Database:
    def __init__(self, db_name: str):
        self.field_col = ['C', 'D', 'E', 'F',
                          'G', 'H', 'I', 'J',
                          'K', 'L', 'M', 'N']
        self.length_col = 'O'
        try:
            self.path = f'dbs/{db_name}.xlsx'
            self.wb = xw.Book(self.path)
        except FileNotFoundError:
            self.wb = xw.Book()
            self.wb.save(self.path)
            print(f"已创建数据库：dbs/{db_name}.xlsx")

        self.config = self.wb.sheets["Sheet1"]

    def create_table(self, table_name: str, pr_key: str, field: list[str]):
        table_length = len(field)

        if len(field) > 12:
            print("create table: 字段数量超过十个了！")
            return
        try:
            _ = self.wb.sheets[table_name]
            print("create table: 已经存在同名表了！")
        except:
            rows = self.config.used_range.last_cell.row
            self.config.range('A' + str(rows + 1)).value = table_name
            self.config.range('B' + str(rows + 1)).value = pr_key
            for i in range(len(field)):
                self.config.range(self.field_col[i] + str(rows + 1)).value = field[i]
            self.config.range(self.length_col + str(rows + 1)).value = table_length
            self.wb.sheets.add(table_name)
            self.wb.save()
            print("create table: 创建成功！！")

    def insert(self, table_name: str, pr_key, field: list[str]):
        try:
            table = self.wb.sheets[table_name]
        except:
            print("insert: 没有该表!")
            return
        if not self.check_field(table_name, field):
            return

        row = 1
        while True:
            x = table.range('B' + str(row)).value
            if x is None:
                table.range('B' + str(row)).value = pr_key
                for i in range(len(field)):
                    table.range(self.field_col[i] + str(row)).value = field[i]
                self.wb.save()
                print(f"insert: 插入成功！pr_key={pr_key}")
                return
            if x == pr_key:
                print(f"insert: 已经存在相同主键{pr_key}")
                return
            elif pr_key < x:
                row = row * 2
            else:
                row = row * 2 + 1

    def select(self, table_name: str, pr_key) -> list[str]:
        try:
            table = self.wb.sheets[table_name]
        except:
            print("select: 没有该表")
            return []

        row = 1
        while True:
            x = table.range('B' + str(row)).value
            if x is None:
                print("select: 没有相应的pr_key")
                return []
            if x == pr_key:
                res = [pr_key]
                for i in range(len(self.field_col)):
                    if table.range(self.field_col[i] + str(row)).value is None:
                        break
                    res.append(table.range(self.field_col[i] + str(row)).value)
                print("select: 找到了符合的数据")
                return res
            elif pr_key < x:
                row = row * 2
            else:
                row = row * 2 + 1

    def update(self, table_name: str, pr_key, field: list) -> None:
        try:
            table = self.wb.sheets[table_name]
        except:
            print("update: 没有该表")
            return

        if not self.check_field(table_name, field):
            return

        row = 1
        while True:
            x = table.range('B' + str(row)).value
            if x is None:
                print("update: 没有相应的pr_key")
                return
            if x == pr_key:
                for i in range(len(self.field_col)):
                    if table.range(self.field_col[i] + str(row)).value is None:
                        break
                    table.range(self.field_col[i] + str(row)).value = field[i]
                self.wb.save()
                print("update: 已更新")
                return
            elif pr_key < x:
                row = row * 2
            else:
                row = row * 2 + 1

    def delete(self, table_name: str, pr_key) -> None:
        try:
            table = self.wb.sheets[table_name]
        except:
            print("delete: 没有该表")
            return

        row = 1
        while True:
            x = table.range('B' + str(row)).value
            if x is None:
                print("delete: 没有相应的pr_key")
                return
            if x == pr_key:
                for i in range(len(self.field_col)):
                    if table.range(self.field_col[i] + str(row)).value is None:
                        break
                    table.range(self.field_col[i] + str(row)).value = None
                table.range('B' + str(row)).value = None
                self.wb.save()
                print("delete: 已更新")
                return
            elif pr_key < x:
                row = row * 2
            else:
                row = row * 2 + 1
    def close(self):
        self.wb.save()
        self.wb.close()

    def check_field(self, table_name: str, field: list) -> bool:
        rows = self.config.used_range.last_cell.row
        for i in range(rows):
            if self.config.range('A' + str(i + 1)).value == table_name:
                field_length = self.config.range(self.length_col + str(i + 1)).value
                if field_length != len(field):
                    print(f"字段数量错误!，应该是{field_length}")
                    return False
                else:
                    return True
