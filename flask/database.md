# 数据库

数据库按照一定规则保存应用的数据，应用再发起查询，取回所需的数据。对中小型应用来说，SQL和NoSQL数据库都是很好的选择，而且性能相当。

## Python数据库框架

选择数据库框架时，要考虑很多因素：

1. 易用性
2. 性能
3. 可移植性
4. Flask集成度

基于以上因素，选择数据库Flask-SQLAlchemy。

## 使用Flask-SQLAlchemy管理数据库

Flask-SQLAlchemy是一个Flask扩展，简化了Flask应用中使用SQLAlchemy的操作。SQLAlchemy是一个强大的关系型数据库框架，支持多种数据库后台。

### 安装

可以使用`pip`安装：

```bash
pip install flask-sqlalchemy
```

### 配置

下面展示如何初始化及配置一个简单的SQLite数据库：

```python
import os
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'GN9rwStf3v1E'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

在Flask-SQLAlchemy中，选择何种数据库，由`SQLALCHEMY_DATABASE_URI`来指定。几种常见的数据库引擎URL格式如下：

|     数据库引擎      |                      URL                      |
| ------------------- | --------------------------------------------- |
| MySQL               | `mysql://username:password@hostname/dabatase` |
| SQLite(Linux,MacOS) | `sqlite:////absolute/path/to/database`        |
| SQLite(windows)     | `sqlite:///C:\\path\\to\\foo.db`              |

SQLAlchemy 暂不支持mongoDB，但可以使用Flask-MongoDB的独立扩展来使用MongoDB数据库。

`SQLALCHEMY_TRACK_MODIFICATIONS`的值设为`False`，可以在不需要追踪对象变化时降低内存消耗。

## 定义模型

**模型**表示应用使用的持久化实体，在ORM中，模型一般是一个类，类的属性对应于数据库表中的列。

Flask-SQLAlchemy创建的数据库实例为模型提供了一个基类以及一系列辅助类和辅助函数，用于定义模型的结构。例如：

```python
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username
```

类变量`__tablename__`定义在数据库中使用的表名，其余的类变量都是该模型的类型。`db.Column`的其他参数可以指定属性的配置选项。

最常用的SQLAlchemy列选项如下：

|   选项名    |                  说明                  |
| ----------- | -------------------------------------- |
| primary_key | 如果设为True，列为表的主键             |
| unique      | 如果为True，列不允许出现重复的值       |
| index       | 如果为True，为列创建索引，提示查询效率 |
| nullable    | 如果为True，列允许使用空值             |
| default     | 为列定义默认值                         |

虽然没有强制要求，但都定义了`__repr()__`方法，返回一个具有可读性的字符串表示模型，供调试和测试时使用。

## 关系

关系型数据库使用关系把不同表中的行联系起来。使用`relationship()`方法建立模型中的关系：

```python
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
```

常用的SQLAlchemy关系选项：

|    选项名     |                         说明                         |
| ------------- | ---------------------------------------------------- |
| backref       | 在关系的另一个模型中添加反向引用                     |
| primaryjoin   | 明确指定两个模型之间使用的连接条件                   |
| lazy          | 指定如何加载相关记录                                 |
| uselist       | 如果设为False，不使用列表，而使用标量值              |
| order_by      | 指定关系中记录的排序方式                             |
| secondary     | 指定多对多关系中关联表的名称                         |
| secondaryjoin | SQLAlchemy无法决定是，指定多对多关系中的二级联结条件 |

## 数据库操作

## 在视图函数中操作数据库

## 集成Python shell

## 使用Flask-Migrate实现数据库迁移

## 参考资料

1. [Flask-SQLAlchemy文档](http://www.pythondoc.com/flask-sqlalchemy/)
1. [SQLAlchemy文档](https://docs.sqlalchemy.org/en/latest/)
