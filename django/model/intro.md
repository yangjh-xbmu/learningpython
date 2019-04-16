# 模型

在 Django 中，**模型**在形式上是定义数据表的文件，并没有提供数据查询之类的功能，这一点，是 Django 框架非常不同与其他框架的地方，Django 将数据查询检索的功能安排在**视图**中。模型包含您数据的重要字段和行为。一般来说，每一个模型都映射一个数据库表。每个模型都是一个 Python 的类，这些类继承 `django.db.models.Model`，模型类的每个属性都相当于一个数据库的字段。Django 会根据字段信息，生成数据库以及访问数据库的 API。

## 创建模型

模型需要继承自`django.db.models.Model`。例如：

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

### 字段类型

Django 框架能根据模型中的字段信息自动生成如下几类信息：

1. 数据表中的字段
1. 表单中对应的HTML元素
1. 后台管理中的HTML页面及表单

在创建模型和字段的时候，和其他变量、类、对象命名一样，不能使用Python的关键字、保留字以及SQL语句中的关键字，也不能使用和Django框架中有冲突的名字。

常用的Django模型字段类型有：

|类型|作用|
|--|--|
|BooleanField|布尔值字段|
|CharField|字符串字段|
|DateField|日期字段|
|DateTimeField|日期时间字段|
|EmailField|电子邮箱字段|
|FileField|文件上传字段|


## 使用模型

1. 定义好模型后，需要修改设置文件中的I`NSTALLED_APPS` ，在这个设置中添加包含你 `models.py` 文件的模块的名字。
2. 在命令行中运行`python manage.py makemigrations`，创建数据库迁移文件。
3. 执行数据库迁移：

   ```bash
   python manage.py migrate
   ```

4. 如有必要，将模型在后台页面中显示出来。
