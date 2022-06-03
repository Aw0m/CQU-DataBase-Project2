# dbProject2
重庆大学计算机学院-数据库project2项目2.通过excel简单实现一个数据库

通过`Database`类实现对excel数据库的操作。

1. 初始化Database类的时候会先判断是否有该数据库(即./db/目录下是否有相应名字的.xlsx的文件)如果没有初始化则会先创建该.xlsx作为数据库。
2. 通过`create_table`, `insert`, `select`, `update`, `delete`四个接口对数据库进行操作。
3. 有基本的错误处理
