# MySQL的存储

成功从页面获取信息后，我们可以将其保存到文件中，也可以存储到数据库中。显然，使用数据库拥有更多后续分析的便利，我们采用常见的关系型数据库MySQL作为信息的保存方式。

## 安装PyMySQL和MySQL

使用Homebrew和pip工具分别安装MySQL和PyMySQL。

## 连接数据库

对数据库的使用和其它语言是一致的，无非就是连接数据库，发送指令，接收结果。

```python
import pymysql
db = pymysql.connect(host='localhost', user='user',password='password', port=3306)
```

使用pymysql的`connect()`方法，设置必要的信息，可以连接到MySQL数据库。

还可以直接连接到MySQL中已经存在的库：

```python
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='passwd',
                             db='db',
                             charset='utf8mb4')
```

## 对数据库进行操作

连接到数据库后，可以使用游标cursor()方法对数据库进行各种操作。

### 创建数据库

使用SQL语句，就可以创建数据库，创建数据库的语句如下：

```python
import pymysql

db = pymysql.connect(host='localhost', user='root',
                     password='mysql', port=3306)

cursor = db.cursor()
sql = "CREATE DATABASE spiders DEFAULT CHARACTER SET utf8"
cursor.execute(sql)
db.commit()
db.close()
```

使用游标方法`cursor()`创建游标对象，用`execute()`方法执行SQL语句，再使用`commit()`提交，最后使用`close()`方法关闭数据库连接。

### 创建数据表

使用SQL语句可以创建数据表，当然前提是连接到数据库。

```python
# coding=utf-8
import pymysql

db = pymysql.connect(host='localhost', user='root',
                     password='mysql', db='spiders')

cursor = db.cursor()
sql = "CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))"
cursor.execute(sql)
db.commit()

db.close()
```

SQL语句的语法，可以参照MySQL参考手册，也可借助于类似phpMyadmin之类的工具进行生成和检测。

### 插入、更新、删除数据

使用INSERT语句，可以插入数据到数据表：

```python
# coding=utf-8
import pymysql

db = pymysql.connect(host='localhost', user='root',
                     password='mysql', db='spiders')

cursor = db.cursor()

id = '2018'
user = 'yangjh'
age = 18

sql = 'INSERT INTO students(id,name,age) values(%s,%s,%s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()
```

插入、更新和删除操作都是对数据库进行更改的操作，这些操作的写法是：

```python
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
```

使用rollback()方法可以回滚执行失败的操作，保持事务的原子性（atomicity），使用异常处理，可以方便地实现业务回滚。

### 查询数据

使用`while`循环加`fetchone()`方法循环获取数据：

```python
sql = 'SELECT * FROM students WHERE age <=20'
try:
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print(row, row[0])
        row = cursor.fetchone()
except:
    print('出错啦！')
db.close()
```

## 参考资料

1. [MySQL手册](https://dev.mysql.com/doc/)
1. [pymysql文档](https://pymysql.readthedocs.io/en/latest/index.html)
